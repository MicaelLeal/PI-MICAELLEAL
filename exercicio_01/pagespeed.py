        ## ---- PageSpeed Insights API ---- ##

    # Descrição:
    #   É uma API do google que analisa o conteúdo
    # de uma página da Web e, em seguida, gera su-
    # gestões para torná-la mais rápida.
    #   Através  do  PageSpeed Insights,  qualquer
    # webmaster pode avaliar a  velocidade de carre-
    # gamento do seu site e melhorar a experiência
    # do seu usuário.

    # link: https://developers.google.com/speed/

import requests

url = input("Url: ")
params = {"url": url}

response = requests.get("https://www.googleapis.com/pagespeedonline/v4/runPagespeed/", params=params)

if response.status_code == 200:
    json = response.json()

    title = json["title"]
    first_display =\
        json["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
    first_interaction_delay = \
        json["loadingExperience"]["metrics"]["DOM_CONTENT_LOADED_EVENT_FIRED_MS"]["category"]
    overall_category =\
        response.json()["loadingExperience"]["overall_category"]

    print("Title: {}\n"
          "Overall category: {}\n"
          "Based on the first content paint: {}\n"
          "Based on the first interaction delay: {}"
          "".format(title, overall_category, first_display, first_interaction_delay))

else:
    print("Error! Check url")