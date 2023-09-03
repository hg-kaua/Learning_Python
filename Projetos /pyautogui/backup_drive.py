#   Abrir o google drive no computador
#   Entrar na area de trabalho
#   Clicar no arquivo e arrastar
#   Enquanto arrasta mudar para pagina do google drive
#   Soltar o arquivo dentro do google drive
#   Esperar alguns segundos

import pyautogui
import time


time.sleep(2)
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")
time.sleep(2)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.keyDown("enter")

