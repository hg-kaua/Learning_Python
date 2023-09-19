from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


lista_noticias = []
# acessar o site do g1
response = requests.get('https://g1.globo.com/')
content = response.content

site = bs(content, 'html.parser')

# html da noticia
noticias = site.findAll('div', attrs={"class":"feed-post-body"})

for noticia in noticias:
    # titulo da noticia
    titulo = noticia.find('a', attrs={"class": "feed-post-link"})
    # subtitulo 
    subtitulo = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
    
    if subtitulo:
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])
        
news = pd.DataFrame(lista_noticias, columns=['Título', 'SubTítulo', 'Link'])
news.to_excel('noticias.xlsx', index=False)
print(news)


