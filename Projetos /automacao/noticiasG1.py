from bs4 import BeautifulSoup as bs
import requests

response = requests.get('https://g1.globo.com/')
content = response.content

site = bs(content, 'html.parser')

# html da noticia
noticia = site.find('div', attrs={"class":"feed-post-body"})

# titulo da noticia
titulo = noticia.find('a', attrs={"class": "feed-post-link"})

# subtitulo 
subtitulo = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})



print(f'\nTítulo: {titulo.text}')
print(f'Subtítulo: {subtitulo.text}')

