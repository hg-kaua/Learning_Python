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
pa.hotkey("ctrl","command", "f")

# fazendo o login

pa.click(x=420, y=229)
pa.typewrite("hugomedeiros")
pa.click(x=393, y=262)
pa.typewrite("Hugo@2323")
pa.click(x=306, y=356)

# inserir dados

# ler os dados
data_frame = pd.read_csv("info_pacote.csv")
data_frame["numero"]
