# Importando o módulo os para trabalhar com variáveis de ambiente e importando as bibliotecas necessárias

import os

import gspread
import requests
import pandas as pd
import telegram
from flask import Flask, request
from flask import Flask, Response
from flask import Response
from oauth2client.service_account import ServiceAccountCredentials
from tchan import ChannelScraper
from bs4 import BeautifulSoup

#Definindo as variáveis de ambiente e escrevendo as credenciais do Google Sheets em um arquivo local

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key("194kfy5ezKLuREJV7UO5mlEkZSYbUMaUQC2q5hi-XKb4")
sheet = planilha.worksheet("robo_lucasduarte_bot")
app = Flask(__name__)  #Criando a aplicação web


#Definindo a página inicial do meu website no Render | Incluindo uma imagem indígena | e mudando a cor de fundo

menu = """
<a href="/">Página inicial</a> | <a href="/noticias">Notícias Indígenas CNN</a> | <a href="/noticias2">Notícias Indígenas Folha de São Paulo</a> | <a href="/noticias3">Noticias Funai</a> | <a href="/sobre">Sobre o site</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Site de Notícias Indígenas</title>
            <style>
                body {
                    background-color: #f1f1f1;
                    font-size: 16px;
                }
            </style>
        </head>
        <body>
            <div style="text-align:center">
                <img src="http://www.prefeitura.sp.gov.br/cidade/secretarias/upload/2018%20Dia%20Povos%20Indigenas.jpg">
            </div>
            <br>
            """ + menu + """
            <br>
            <p>Olá, seja bem-vindo(a) ao site de notícias indígenas do jornalista Lucas Duarte</p>
        </body>
    </html>
    """

#Definindo a página sobre e escrevendo um pouco sobre o trabalho | Definindo a página Contato
  
@app.route("/sobre")
def sobre():
  return menu + "Robô de notícias indígenas: A análise de dados é uma ferramenta poderosa para a compreensão de tendências e padrões em diversos setores da sociedade. No contexto dos povos indígenas, a análise de notícias diárias pode ajudar a identificar padrões de violação de direitos humanos e a mapear a presença dessas comunidades em diferentes regiões. Nesse sentido, a utilização do método de raspagem em Python pode ser uma ferramenta valiosa para coletar e analisar notícias diárias sobre indígenas."

@app.route("/contato")
def contato():
  return menu + "Mais informações: Lucas Duarte, jornalista | lucasduartematos@gmail.com | (91) 981235649"

#Definindo a rota para a página de notícias dos sites CNN, Folha de São Paulo e as notícias da FUNAI

@app.route("/noticias")
def noticias_indigenas():
    requisicao=requests.get('https://www.cnnbrasil.com.br/tudo-sobre/indigenas/')
    html=BeautifulSoup(requisicao.content)
    manchetes_indigenas=html.findAll('li',{'class':'home__list__item'})
    lista_noticias=[]
    for noticia in manchetes_indigenas:
        manchete=noticia.text
        link=noticia.find('a')['href']
        link_html = f'<a href="{link}">{link}</a>'
        lista_noticias.append([manchete, link_html])
    df=pd.DataFrame(lista_noticias, columns=['Manchete','Link'])
    tabela_html = df.to_html(escape=False)
    return Response(tabela_html, mimetype='text/html')
    
@app.route("/noticias2")
def noticias_indigenas_folha():
    requisicao=requests.get('https://www1.folha.uol.com.br/folha-topicos/indigenas/')
    html=BeautifulSoup(requisicao.content)
    manchetes_indigenas_folha=html.findAll('div',{'class':'c-headline c-headline--newslist'})
    lista_noticias=[]
    for noticia in manchetes_indigenas_folha:
        manchete = noticia.find('h2').text.strip()
        link = noticia.find('a')['href'] 
        lista_noticias.append([manchete, link])
    
    for i, row in enumerate(lista_noticias):
        lista_noticias[i][0] = row[0].replace('notícias para assinantes - ', '')
    
    df=pd.DataFrame(lista_noticias, columns=['Manchete','Link'])
    df['Link'] = df['Link'].apply(lambda x: f"<a href='{x}'>{x}</a>")
    tabela_html = df.to_html(escape=False)
    return Response(tabela_html, mimetype='text/html')
  
@app.route("/noticias3")
def noticias_funai():
    url = 'https://www.gov.br/funai/pt-br/assuntos/noticias/2023'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    noticias = soup.find_all('div', {'class': 'conteudo'})
    lista_noticias = []
    for noticia in noticias:
        link = noticia.find('a')['href']
        titulo = noticia.find('a').text.strip()
        # Adiciona a tag "a" com o atributo "href" ao link da notícia
        link_html = f'<a href="{link}">{link}</a>'
        lista_noticias.append([titulo, link_html])
    df = pd.DataFrame(lista_noticias, columns=['Título', 'Link'])
    # Substitui a coluna 'Link' pela coluna HTML
    df['Link'] = df['Link'].apply(lambda x: BeautifulSoup(x, 'html.parser').prettify())
    tabela_html = df.to_html(escape=False, index=False)
    return Response(tabela_html, mimetype='text/html')

#Executando a aplicação Flask                    
  
if __name__ == '__main__':
  app.run()
  


