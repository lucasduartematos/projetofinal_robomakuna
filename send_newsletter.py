import sendgrid
import os
from sendgrid.helpers.mail import *
import requests
from bs4 import BeautifulSoup
import pandas as pd

# definindo a função de envio de email
def send_email(to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("lucasduartematos@gmail.com")
    to_email = To(to_email)
    content = Content("text/plain", content)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response

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
    # selecione as 5 notícias mais recentes
    top_noticias = df.head(5)
    # criando a tabela HTML das notícias
    tabela_html = top_noticias.to_html(escape=False)
    # envie as notícias por email
    to_email = "lucasduartematos@gmail.com"
    subject = "As 5 notícias mais recentes dos indígenas na Folha"
    content = "Aqui estão as 5 notícias mais recentes dos indígenas na Folha:<br><br>" + tabela_html
    response = send_email(to_email, subject, content)
    if response.status_code == 202:
        return "As notícias foram enviadas por email com sucesso!"
    else:
        return "Houve um problema ao enviar as notícias por email. Tente novamente mais tarde."
