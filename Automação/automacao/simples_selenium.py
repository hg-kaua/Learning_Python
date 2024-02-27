from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Crie o driver do Selenium com as opções configuradas
navegador = webdriver.Chrome(options=options)
navegador.get("http://www.python.org")

element = navegador.find_element("xpath", '//*[@id="documentation"]/a')
element.click()

# print(navegador.title)
# navegador.back()
# navegador.back()


navegador.quit()