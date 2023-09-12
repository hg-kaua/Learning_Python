import requests
from tkinter import *


def pegar_cotacoes():
    moeda = nome_caixa_opc.get()
    
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_disc = requisicao.json()
    

    cotacao_dolar = requisicao_disc["USDBRL"]["bid"] 
    cotacao_euro = requisicao_disc["EURBRL"]["bid"]
    cotacao_bitcoin = requisicao_disc["BTCBRL"]["bid"]
    
    if moeda == "Dólar":
        texto = f"Dólar: {cotacao_dolar}"
    elif moeda == "Euro":
        texto = f"Euro: {cotacao_euro}"
    elif moeda == "Bitcoin":
        texto = f"Bitcoin: {cotacao_bitcoin}"
        
    texto_cotacoes["text"] = texto
    
# ------- Criando a interface ---------h

# Sempre iniciar assim
janela = Tk()

janela.title("Cotaçao Moedas")
# tamanho da janela
janela.geometry("400x400")

# Label é um texto dentro da janela
texto_orientacao = Label(janela, text="Escolha a moeda no menu ao lado") 
# Primeiro cria o texto depois fala a posiçao dele atraves do grid
texto_orientacao.grid(column=0, row=0, padx=20, pady=10)

nome_caixa_opc = StringVar(janela)
nome_caixa_opc.set("Moedas")
escolher_moeda = OptionMenu(janela, nome_caixa_opc, "Dólar", "Euro", "Bitcoin")
escolher_moeda.grid(column=1, row=0)


botao = Button(janela, text="Buscar cotação", command=pegar_cotacoes)
botao.grid(column=0,row=1, padx=20, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=1, row=1, padx=20, pady=10)


# Sempre finalizar assim
janela.mainloop()