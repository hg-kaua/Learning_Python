import pyautogui as pa
import time
import pandas as pd


# abrindo pagina de login

pa.PAUSE = 1
pa.keyDown("command")
pa.press("space")
pa.keyUp("command")
pa.typewrite("Login.xlsx")
pa.press("enter")
time.sleep(2)
pa.hotkey("ctrl","command", "f")
pa.click(x=97, y=862)
time.sleep(1)

# fazendo o login

time.sleep(1)
pa.click(x=420, y=229)
pa.typewrite("hugomedeiros")
pa.click(x=393, y=262)
pa.typewrite("Hugo@2323")
pa.click(x=306, y=356)

# inserir dados

# ler os dados
data_frame = pd.read_csv("info_pacote.csv")
i = 0
time.sleep(1)
for linha in data_frame.values:
    numero_rastre = data_frame["Número de Rastreamento"][i]
    pa.click(x=311, y=347, duration=1)
    time.sleep(1)
    pa.write(numero_rastre)
    nome_dest = data_frame["Nome do Destinatário"][i]
    pa.click(x=429, y=348, duration=1)
    time.sleep(1)
    pa.write(nome_dest)
    data_entrega = data_frame["Data de Entrega"][i]
    pa.click(x=580, y=345, duration=1)
    time.sleep(1)
    pa.write(data_entrega)
    categoria_prod = data_frame["Categoria do Produto"][i]
    pa.click(x=709, y=343, duration=1)
    time.sleep(1)
    pa.write(categoria_prod)
    i+=1

