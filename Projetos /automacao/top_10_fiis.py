from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep


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
    
    sleep(0.5)
    dy_min.send_keys('800')
    dy_max.clear()
    dy_max.send_keys('1400')
    
    # inserindo preço sobre valor patrimonial desejado
    p_vp_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[2]/div/div[2]/div[1]/input')
    p_vp_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[2]/div/div[2]/div[2]/input')

    sleep(0.5)
    p_vp_min.send_keys('080')
    p_vp_max.clear()
    p_vp_max.send_keys('150')
    
    sleep(0.5)
    num_cotista = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[4]/div/div[2]/div[1]/input')
    num_cotista.send_keys('6500000')
    
    sleep(0.5)
    
    cagr = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[2]/div[5]/div/div[2]/div[1]/input')
    cagr.send_keys('500')
    
    search = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
    search.click()
    
    pass

def analisar_acao():
    
    # inserindo dividend yild desejado
    dy_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[1]/div/div[2]/div[1]/input')
    dy_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[1]/div/div[2]/div[2]/input')
    
    sleep(0.5)
    dy_min.send_keys('800')
    dy_max.clear()
    dy_max.send_keys('1400')
    
    # inserindo preço sobre valor patrimonial desejado
    p_vp_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[4]/div/div[2]/div[1]/input')
    p_vp_max = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[4]/div/div[2]/div[2]/input')

    sleep(0.5)
    p_vp_min.send_keys('80')
    p_vp_max.clear()
    p_vp_max.send_keys('150')
    
    # inserindo margem liquida
    margem_liquida_min = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[8]/div/div[2]/div[1]/input')
    margem_liquida_min.send_keys('1000')
    
    # inserindo o roe
    roe = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/form/div[4]/div[16]/div/div[2]/div[1]/input')
    roe.send_keys('1000')
    
    search = nav.find_element('xpath', '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
    search.click()
    
    pass

def recolher_investimento():
    site = bs(nav.page_source, 'html.parser')
    
    papeis = site.findAll('span', attrs={"class": "ticker waves-effect"})
    
    for papel in papeis:
        preco = site.find('td', attrs={"class": "text-right"})
        
        dy = site.find('td', attrs={"data-key": "dy"})
        
        p_vp = site.find('td', attrs={"data-key": "p_vp"})
        
        margem_liquida = site.find('td', attrs={"data-key": "margemliquida"})
        
        print(f'Papel: {papel.text}')
        print(f'Preço: {preco.text}')
        print(f'DY: {dy.text}')
        print(f'P/VP: {p_vp.text}')
        
        if margem_liquida:
            print(f'Margem líquida: {margem_liquida.text}')
        
        print()
    

investimento = selecionar_investimento()

nav = webdriver.Chrome(options=options)
print(nav.get(url_base + investimento))



sleep(2)

if opcao == '1':
    analisar_acao()
    sleep(2)
    recolher_investimento()
    sleep(10)
    nav.quit()
elif opcao == '2':
    sleep(2)
    analisar_fii()
    sleep(10)
    recolher_investimento()
    nav.quit()

