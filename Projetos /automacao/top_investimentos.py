from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import pandas as pd




tempo = 0.5
lista_parametros = ['800', '1000']

options = webdriver.ChromeOptions()
# options.add_argument('-headless')
options.add_experimental_option("detach", True)

url_base = 'https://statusinvest.com.br/'

opcao = input("O que deseja procurar (1 - acao/ 2 -fundos imobiliarios)? ")



def selecionar_investimento():  
    return 'acoes/busca-avancada' if opcao == '1' else 'fundos-imobiliarios/busca-avancada'

def analisar_fii():
    
    # inserindo dividend yild desejado
    dy_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[1]/div/div[2]/div[1]/input')
    dy_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[1]/div/div[2]/div[2]/input')
    
    sleep(tempo)
    dy_min.send_keys(lista_parametros[0])
    dy_max.clear()
    dy_max.send_keys('1400')
    
    # inserindo preço sobre valor patrimonial desejado
    p_vp_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[2]/div/div[2]/div[1]/input')
    p_vp_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[2]/div/div[2]/div[2]/input')

    sleep(tempo)
    p_vp_min.send_keys('080')
    p_vp_max.clear()
    p_vp_max.send_keys('150')
    
    sleep(tempo)
    num_cotista = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[4]/div/div[2]/div[1]/input')
    num_cotista.send_keys('6500000')
    
    sleep(tempo)
    
    cagr = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[5]/div/div[2]/div[1]/input')
    cagr.send_keys('500')
    
    search = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
    search.click()
    
    pass

def analisar_acao():
    
    # inserindo dividend yild desejado
    dy_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[1]/div/div[2]/div[1]/input')
    dy_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[1]/div/div[2]/div[2]/input')
    
    sleep(tempo)
    dy_min.send_keys(lista_parametros[0])
    dy_max.clear()
    dy_max.send_keys('1400')
    
    # inserindo preço sobre valor patrimonial desejado
    p_vp_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[4]/div/div[2]/div[1]/input')
    p_vp_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[4]/div/div[2]/div[2]/input')

    sleep(tempo)
    p_vp_min.send_keys('80')
    p_vp_max.clear()
    p_vp_max.send_keys('150')
    
    # inserindo margem liquida
    margem_liquida_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[8]/div/div[2]/div[1]/input')
    margem_liquida_min.send_keys(lista_parametros[1])
    
    # inserindo o roe
    roe = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[16]/div/div[2]/div[1]/input')
    roe.send_keys(lista_parametros[1])
    
    search = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
    search.click()
    
    pass

def recolher_investimento():
    site = bs(nav.page_source, 'html.parser')
    
    papeis = site.findAll('span', attrs={"class": "ticker waves-effect"})
    preco = site.findAll('td', attrs={"data-key": "price"})
    dy = site.findAll('td', attrs={"data-key": "dy"})
    p_vp = site.findAll('td', attrs={"data-key": "p_vp"})
    margem_liquida = site.findAll('td', attrs={"data-key": "margemliquida"})
    
    index = 0
    lista_investimento = []
    
    for papel in papeis:
        print(f'Papel: {papel.text}')
        print(f'Preço: {preco[index].text}')
        print(f'DY: {dy[index].text}')
        print(f'P/VP: {p_vp[index].text}')
        
        if margem_liquida:
            print(f'Margem líquida: {margem_liquida[index].text}')
            lista_investimento.append([papel.text, preco[index].text, dy[index].text, p_vp[index].text, margem_liquida[index].text])
        else:
            lista_investimento.append([papel.text, preco[index].text, dy[index].text, p_vp[index].text])
        
        index+=1
        print()
        
    return lista_investimento


# transformar lista em xlsx

def converter_excel(dado, name):
    if len(dado[0]) == 5:
        df = pd.DataFrame(dados, columns=["Papel", "Preço", "Dividend Yield", "P/VP", "Margem líquida"])
        print(df)
    else:
        df = pd.DataFrame(dados, columns=["Papel", "Preço", "Dividend Yield", "P/VP"])
        print(df)
    
    nome_arq = 'melhores_' + name + '.xlsx'
    df.to_excel(nome_arq, index=False)
    
investimento = selecionar_investimento()

nav = webdriver.Chrome(options=options)
nav.get(url_base + investimento)
sleep(2)

if opcao == '1':
    sleep(2)
    analisar_acao()
    recolher_investimento()
    dados = recolher_investimento()
    sleep(1)
    converter_excel(dados,"açoes")
    sleep(10)
    nav.quit()
elif opcao == '2':
    sleep(2)
    analisar_fii()
    recolher_investimento()
    dados = recolher_investimento()
    sleep(1)
    converter_excel(dados,"fiis")
    sleep(10)
    nav.quit()

