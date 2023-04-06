import os

import gspread
import requests
import pandas as pd
from flask import Flask, Response
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import telegram


TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
with open("credenciais.json", mode="w") as arquivo:
    arquivo.write("{}\n".format(GOOGLE_SHEETS_CREDENTIALS))

conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key("194kfy5ezKLuREJV7UO5mlEkZSYbUMaUQC2q5hi-XKb4")
sheet = planilha.worksheet("robo_lucasduarte_bot")

app = Flask(__name__)

bot = telegram.Bot(token=TELEGRAM_API_KEY)


@app.route("/noticias")
def noticias_indigenas():
    requisicao = requests.get('https://www.cnnbrasil.com.br/tudo-sobre/indigenas/')
    html = BeautifulSoup(requisicao.content)
    manchetes_indigenas = html.findAll('li', {'class': 'home__list__item'})
    lista_noticias = []
    for noticia in manchetes_indigenas[:5]:  # seleciona apenas as 5 primeiras notícias
        manchete = noticia.text
        link = noticia.find('a').get('href')
        lista_noticias.append([manchete, link])
        mensagem = f"<b>{manchete}</b>\n<a href='{link}'>Leia a notícia completa</a>"
        bot.send_message(chat_id=TELEGRAM_ADMIN_ID, text=mensagem, parse_mode=telegram.ParseMode.HTML)
    df = pd.DataFrame(lista_noticias, columns=['Manchete', 'Link'])
    tabela_html = df.to_html()
    return Response(tabela_html, mimetype='text/html')


def planilha(df):
    lista = df.values.tolist()
    sheet.append_rows(lista)
    return "Planilha escrita!"


if __name__ == '__main__':
    app.run()
