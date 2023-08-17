from tkinter import *
from tkinter import ttk


# construindo do zero calculadora de IMC

def calcular_imc():
    pass

# construindo interface grafica
janela = Tk()

janela.title("Calculadora IMC")
janela.geometry("400x200")
# campo peso
texto_peso = Label(text="Informe seu peso: ", padx=10, pady=10)
texto_peso.grid(column=0, row=0)
entrada_peso = Entry(janela, width=4)
entrada_peso.grid(column=1, row=0)

# campo altura
texto_altura = Label(text="Informe sua altura: ", padx=10, pady=10)
texto_altura.grid(column=0, row=1)
entrada_altura = Entry(janela, width=4)
entrada_altura.grid(column=1,row=1)

# botao calcular
botao_calcular = Button(janela,text= "Calcular IMC", width=10, height=2, command=calcular_imc)
botao_calcular.grid(column=0, row=3)

janela.mainloop()