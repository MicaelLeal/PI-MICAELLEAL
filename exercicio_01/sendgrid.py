        ## ---------- SendGrid ---------- ##

    # Descrição:
    #   O SendGrid é um serviço de e-mail baseado
    # em nuvem que oferece entrega de e-mail tran-
    # sacional, escalabilidade e análise em tempo
    # real confiáveis com APIsflexíveis que faci-
    # litam a integração personalizada.

    # Os cenários comuns de uso:
    # * Envio automático de recibos para os clientes;
    # * Administração de listas de distribuição para
    #   envio mensal de panfletos eletrônicos e ofer-
    #   tas especiais aos clientes;
    # * Coleta  de métricas em  tempo real para, por
    #   exemplo, email bloqueado e capacidade de res-
    #   posta do cliente;
    # * Encaminhamento de consultas dos clientes;

    # link:https://sendgrid.com/


import requests

url = "https://api.sendgrid.com/api/mail.send.json"
username = "MicaelLeal"
key = "**********"

payload = {
    "api_user": username,
    "api_key": key,
    "to": "mycaellmoura@hotmail.com",
    "toname": "Micael leal",
    "subject": "Hello world!",
    "text": "Iai man, vai da certo ou não vai?!",
    "from": "mycaellmoura@gmail.com"
}

response = requests.post(url, data=payload)

print(response.status_code)
print(response.content)