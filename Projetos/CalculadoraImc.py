from tkinter import *
from tkinter import ttk

# cores

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#4065a1"  # vermelha


# Criando janela e configurando
janela = Tk()

janela.title("")
janela.geometry("295x230")
janela.configure(bg=co0)



# Adicionando frames cima e baixo

frame_cima = Frame(janela, width=95, height=50, bg=co1, pady=0, padx=0, relief="flat")
frame_cima.grid(row=1, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=200,bg=co1, pady=0, padx=0, relief="flat",)
frame_baixo.grid(row=1, column=0, sticky=NSEW)
 
style = ttk.Style(janela)
style.theme_use("clam")

# frame_cima = Frame(janela, width=295, height=50,bg=co1, pady=0, padx=0, relief="flat",)
# frame_cima.grid(row=0, column=0, sticky=NSEW)
 
# frame_baixo = Frame(janela, width=295, height=200,bg=co1, pady=0, padx=0, relief="flat",)
# frame_baixo.grid(row=1, column=0, sticky=NSEW)
 
# style = ttk.Style(janela)
# style.theme_use("clam")


# Configurando frame cima

app_nome = Label(frame_cima, text="Calculadora de IMC", width=23,height=1, padx=0, relief="flat", anchor="center", font=('Ivy 16 bold'), bg=co1, fg=co0)
app_nome.place(x=0, y=2)
 
app_linha = Label(frame_cima, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

janela.mainloop()
