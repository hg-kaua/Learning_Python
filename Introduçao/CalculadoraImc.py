from tkinter import *
from tkinter import ttk


# construindo do zero calculadora de IMC

def calcular_imc():
    # Abaixo do peso = menos de 18,5
    # Normal = maior ou igual a 18,5 e menor que 25
    # Sobrepeso = maior ou igual a 25 e menor que 30
    # Obesidade = 30 ou mais
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())**2
    
    imc = peso / altura
    print(imc)
    
    if imc < 18.5:
        resultado = f"Seu IMC é igual {imc:.2f} - Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        resultado = f"Seu IMC é igual {imc:.2f} - Normal"
    elif imc >= 25 and imc < 30:
        resultado = f"Seu IMC é igual {imc:.2f} - Sobrepeso"
    elif imc >= 30:
        resultado = f"Seu IMC é igual {imc:.2f} - Obesidade"
    else:
        resultado = f"Não foi possível calcular seu IMC"
    
    texto_resultado["text"] = resultado
        

# construindo interface grafica
janela = Tk()

janela.title("Calculadora IMC")
janela.geometry("600x200")


frame_cima = Frame(width=600, height=10, bg="#444466", relief="flat", pady=20)
frame_cima.grid(column=0,row=0)
# campo peso
texto_peso = Label(janela,text="Informe seu peso: ", padx=10, pady=10, relief="flat")
texto_peso.grid(column=0, row=2, sticky= W)
entrada_peso = Entry(janela, width=4, relief="flat")
entrada_peso.grid(column=0, row=2)

# campo altura
texto_altura = Label(janela, text="Informe sua altura: ", padx=10, pady=10)
texto_altura.grid(column=0, row=3, sticky= W)
entrada_altura = Entry(janela, width=4)
entrada_altura.grid(column=0,row=3)

# botao calcular
botao_calcular = Button(janela,text= "Calcular IMC", width=10, height=2, command=calcular_imc)
botao_calcular.grid(column=0, row=4, sticky= W)

texto_resultado = Label(janela, text="", relief="flat")
texto_resultado.grid(column=0, row=5, sticky= W)

janela.mainloop()