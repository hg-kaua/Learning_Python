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

texto_resultado = Label(janela, text="",relief="flat", anchor="center")
texto_resultado.grid(column=5, row=3)

janela.mainloop()