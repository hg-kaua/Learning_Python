import pyautogui as pa
import pandas as pd

data_frame = pd.read_csv("info_pacote.csv")

colunas = data_frame.columns

print(colunas)

