from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url_base = 'https://statusinvest.com.br/'

def selecionar_investimento():  
    investimento = input("O que deseja procurar (1 - acao/ 2 -fundos imobiliarios)? ")
    return 'acoes/busca-avancada' if investimento == '1' else 'fundos-imobiliarios/busca-avancada'

def analisar_fii():
    
    # inserindo dividend yild desejado
    dy_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[1]/div/div[2]/div[1]/input')
    dy_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[1]/div/div[2]/div[2]/input')
    
    sleep(0.5)
    dy_min.send_keys('8,00')
    dy_max.clear()
    dy_max.send_keys('14,00')
    
    # inserindo preço sobre valor patrimonial desejado
    p_vp_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[2]/div/div[2]/div[1]/input')
    p_vp_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[2]/div/div[2]/div[2]/input')

    sleep(0.5)
    p_vp_min.send_keys('0,80')
    p_vp_max.clear()
    p_vp_max.send_keys('1,10')
    
    sleep(0.5)
    num_cotista = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[4]/div/div[2]/div[1]/input')
    num_cotista.send_keys('55,000')
    
    sleep(0.5)
    
    cagr = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[6]/div/div[2]/div[1]/input')
    cagr.send_keys('20,00')
    
    search = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
    search.click()
    
    pass

def analisar_acao():
    pass

investimento = selecionar_investimento()

nav = webdriver.Chrome(options=options)
print(nav.get(url_base + investimento))



sleep(2)
analisar_fii()


sleep(10)
nav.quit()
