import getpass
import requests

WEBHOOK_URL = "https://trabalhofinal-algoritimosdeautomacao.onrender.com/noticias"

def ativar_webhook():
    dados = {"url": WEBHOOK_URL}
    resposta = requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook", data=dados)
    print(resposta.text)

if __name__ == '__main__':
    ativar_webhook()
