    # Pocket API

# Pocket é um aplicativo quetraz o
# "poder do salvar para depois".
# Funciona como um bolso, onde você
# pode pegar sites e páginas na internet
# e deixá-los armazenados e organizados.
# A API traz a possibilidade de usar
# essas funções em qualquer site ou app.

# link: https://getpocket.com/developer/

import requests

consumer_key = "{consumer key}"
code = "{code}"
access_token = "{access_token}"
username = "mycaellmoura%40gmail.com"
url = "http://www.ifpi.edu.br"

data = {
    "ulr": url,
    "consumer_key": consumer_key,
    "access_token": access_token,
    "titulo": "Home — IFPI Instituto Federal do Piauí"
}

response = requests.post("https://getpocket.com/v3/add", params=data)

print(response.content)
print(response.status_code)

