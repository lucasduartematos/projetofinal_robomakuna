import os

import requests
import pandas as pd
import telegram
from flask import Flask, request, render_template, Response
from bs4 import BeautifulSoup


TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
bot = telegram.Bot(token=TELEGRAM_API_KEY)
app = Flask(__name__)

menu = """
<a href="/">Página inicial</a> | <a href="/noticias">Notícias Indígenas</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return menu + "Olá, seja bem-vindo(a) ao site de notícias indígenas do jornalista Lucas Duarte"

@app.route("/sobre")
def sobre():
  return menu + "Robô de notícias indígenas: A análise de dados é uma ferramenta poderosa para a compreensão de tendências e padrões em diversos setores da sociedade. No contexto dos povos indígenas, a análise de notícias diárias pode ajudar a identificar padrões de violação de direitos humanos e a mapear a presença dessas comunidades em diferentes regiões. Nesse sentido, a utilização do método de raspagem em Python pode ser uma ferramenta valiosa para coletar e analisar notícias diárias sobre indígenas."

@app.route("/contato")
def contato():
  return menu + "Mais informações: lucasduartematos@gmail.com"

@app.route("/noticias")
def noticias_indigenas():
    requisicao=requests.get('https://site-projeto-robomakuna.onrender.com/noticias')
    html=BeautifulSoup(requisicao.content)
    manchetes_indigenas=html.findAll('h2',{'class':'titulo'})
    lista_noticias=[]
    for noticia in manchetes_indigenas:
        manchete=noticia.text.strip()
        link=noticia.find('a').get('href')
        lista_noticias.append([manchete, link])
    df=pd.DataFrame(lista_noticias, columns=['Manchete','Link'])
    df_top5 = df[:5]
    noticias = []
    for index, row in df_top5.iterrows():
        noticias.append(f"{index+1}. {row['Manchete']} - {row['Link']}")
    mensagem = "\n".join(noticias)
    bot.send_message(chat_id=TELEGRAM_ADMIN_ID, text=mensagem)
    return "Notícias enviadas para o chat no Telegram!"

if __name__ == "__main__":
    app.run()
