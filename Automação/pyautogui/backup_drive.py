#   Abrir o google drive no computador
#   Entrar na area de trabalho
#   Clicar no arquivo e arrastar
#   Enquanto arrasta mudar para pagina do google drive
#   Soltar o arquivo dentro do google drive
#   Esperar alguns segundos

import pyautogui
import time

time.sleep(5)

# abrindo o spotlight para abrir o chrome
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")
time.sleep(2)
pyautogui.write("chrome")
pyautogui.keyDown("enter")

# comando que cria nova aba no chrome
pyautogui.hotkey("command", "t")

# escrevendo o caminho para o drive 
time.sleep(2)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.keyDown("enter")




