**PROJETOFINAL_ROBOMAKUNA:**
O Makuna é o projeto final do aluno Lucas Duarte Matos, feito no Master de Jornalismo de Dados, Automação e Data Storytelling do Insper. O robô raspa notícias sobre indígenas no site da CNN e Folha de São Paulo e transforma em um dataframe com manchetes e links atualizados diariamente e armazenados em um website do render.

*"Makuna" é uma palavra que tem origem na língua indígena Tukano, falada por povos que habitam a região amazônica do Brasil, Colômbia e Venezuela. O termo pode ter diferentes significados dependendo do contexto, mas geralmente é associado à ideia de força, coragem e resiliência.*


>> **Análise de dados de notícias sobre indígenas no Brasil**

A análise de dados é uma ferramenta poderosa para a compreensão de tendências e padrões em diversos setores da sociedade. 
No contexto dos povos indígenas, a análise de notícias diárias pode ajudar a identificar padrões de violação de direitos humanos e a mapear a presença dessas comunidades 
em diferentes regiões. Nesse sentido, a utilização do método de raspagem em Python pode ser uma ferramenta valiosa para coletar e analisar notícias diárias sobre 
indígenas.

A raspagem de dados é uma técnica utilizada para coletar informações de fontes públicas disponíveis na internet, como sites de notícias e redes sociais. 
Através do uso de bibliotecas Python, é possível extrair informações relevantes dessas fontes e organizá-las em um formato estruturado, como uma planilha ou um banco de 
dados. Dessa forma, é possível analisar esses dados e identificar tendências e padrões relevantes para a compreensão do contexto dos povos indígenas.

Ao aplicar o método de raspagem em Python na análise de notícias sobre indígenas diariamente, é possível criar um banco de dados atualizado e organizado sobre as violações
de direitos humanos e a presença dessas comunidades em diferentes regiões. Essa análise pode ser utilizada para subsidiar a formulação de políticas públicas e o 
desenvolvimento de estratégias de defesa dos direitos dessas populações.

Em suma, o método de raspagem em Python é uma ferramenta poderosa para a análise de notícias diárias sobre indígenas. Ao coletar e organizar informações relevantes em um f
ormato estruturado, é possível identificar padrões e tendências importantes para a compreensão do contexto dessas comunidades e para a formulação de políticas públicas 
voltadas para a defesa de seus direitos.

> **O Trabalho realizado fez raspagem dos sites de notícias CNN e Folha de São Paulo, e notícias da FUNAI pelo termo "indígenas" e transformou manchetes e links em um dataframe.
Os dados da planilha foram armazenados em um website por meio do Render e são atualizados diariamente com o uso do Pipedream. O site é automatizado para rodar os códigos 
todos os dias, às 11h da manhã (o da CNN) e a cada 5h (o da Folha de São Paulo). A próxima etapa almejada no trabalho é enviar as notícias mais recentes para uma newsletter no email usando a biblioteca SendGrid e criar um robô no telegram que envie todos os dias as 5 notícias mais atuais.** 

**SOBRE O CÓDIGO:**

Este código é um programa em Python que cria um website usando o Flask, uma biblioteca para desenvolvimento web em Python. O website mostra notícias sobre indígenas de dois sites diferentes e da página de notícias da FUNAI e possui links para outras páginas, como a página inicial, a página "sobre" e a página "contato". O código também usa bibliotecas Python, como gspread (para se comunicar com o Google Sheets) e BeautifulSoup (para raspar os dados dos sites de notícias).

Na primeira etapa, o código importa bibliotecas como gspread, requests, e pandas, que serão usadas para executar as funções do website. Em seguida, o código define as informações da API do Telegram, o ID do administrador do Telegram e as credenciais do Google Sheets usando o módulo os e o ServiceAccountCredentials do oauth2client. O código cria um arquivo chamado credenciais.json para armazenar as credenciais do Google Sheets. Em seguida, o código usa a biblioteca gspread para autorizar as credenciais e abrir a planilha especificada pelo seu ID e nome da planilha.

Em seguida, o código define uma função para criar um objeto Flask que será usado para executar o website. O código define uma variável de menu que contém links para as diferentes páginas e define rotas para cada uma dessas páginas usando o decorator @app.route. A primeira rota é para a página inicial, que mostra uma imagem e uma mensagem de boas-vindas. A segunda rota é para a página "sobre", que descreve a motivação para criar um robô de notícias indígenas usando a raspagem de dados em Python. A terceira rota é para a página "contato", que fornece informações de contato para o jornalista responsável pelo robô de notícias.

As outras rotas são para as páginas que exibem as notícias. A quarta rota, "/noticias", raspa as manchetes de notícias sobre indígenas do site da CNN Brasil usando a biblioteca BeautifulSoup e exibe uma tabela HTML com as manchetes e os links correspondentes. A quinta rota, "/noticias2", faz a mesma coisa para o site da Folha de São Paulo e a quinta rota "/noticias3", faz a raspagem na busca de notícias da página da FUNAI.

Por fim, o código executa o objeto Flask criado anteriormente usando a função run(). Quando o programa é executado, o website fica disponível em um endereço local (https://site-projeto-robomakuna.onrender.com/) e pode ser acessado por meio de um navegador da web.

**Para mais informações:** 
lucasduartematos@gmail.com | (91) 981235649
