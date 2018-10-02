import requests
import re
from bs4 import BeautifulSoup
import time

all_links = {}

def remover_scripts(soup):
	for script in soup(["script", "style"]):
		script.extract()


def encontrar_palavra(key: str, texto: str):
    return re.findall('\w*.{0,10}' + key + '.{0,20}\w*', texto, re.IGNORECASE)


def buscar_recursiva(url: str, camada: int, palavra: str):

	try:
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	except Exception as e:
		#print('Link: %s\nErro: %s\n' % (url, e))
		return


	if (camada <= 0):

		remover_scripts(soup)

		resultado = '## Resultados para o link: '+ url +'\n'
		encontrados = encontrar_palavra(palavra, soup.text)

		if len(encontrados) == 0:
			#print(resultado+'Nenhum resustado para este link!\n')
			return

		for trecho in encontrados:
			resultado += '"[...]%s[...]"\n' %trecho

		print(resultado)

	else:
		links = soup.findAll('a')

		for link in links:
			link_href = link.get('href')

			if type(link_href) is str and link_href.startswith("http"):
				if link_href in all_links:
					continue

				all_links[link_href] = 0

				buscar_recursiva(link_href, camada-1, palavra)


def main():
	ini = time.time()

	url = input('Url: ')
	key = input('Buscar: ')
	camada = int(input('Profundidade: '))

	buscar_recursiva(url, camada, key)

	fim = time.time()

	print(len(all_links))
	print((fim-ini)/60)


if __name__ == '__main__':
	main()


