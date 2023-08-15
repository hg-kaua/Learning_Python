import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    
    requisicao_disc = requisicao.json()
    
    cotacao_dolar = requisicao_disc["USDBRL"]["bid"] 
    cotacao_euro = requisicao_disc["EURBRL"]["bid"]
    cotacao_bitcoin = requisicao_disc["BTCBRL"]["bid"]
    
    print(f"""
          Dólar: {cotacao_dolar}
          Euro: {cotacao_euro}
          Bitcoin: {cotacao_bitcoin}
          """)
    
# ------- Criando a interface ---------h

# Sempre iniciar assim
janela = Tk()

janela.title("Cotaçao Moedas")

# Label é um texto dentro da janela
texto_orientacao = Label(janela, text="Clique no botao para exibir as cotações")
# Primeiro cria o texto depois fala a posiçao dele atraves do grid
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0,row=1)

texto_cotacoes = Label(janela, text="ainda nao cliq")
# Sempre finalizar assim
janela.mainloop()