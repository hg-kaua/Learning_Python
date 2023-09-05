import pyautogui as pa
import time
# from mouseinfo import mouseInfo

# mouseInfo()

# abrindo o apple music
time.sleep(2)
pa.keyDown("command")
pa.press("space")
pa.keyUp("command")
time.sleep(1)
pa.write("musica")
pa.press("enter")
time.sleep(3)
pa.click(172,141, duration=2)
pa.hotkey("command", "backspace")
pa.write("os planos de deus")
pa.press("enter")
pa.click(325,227, duration=2)


# abrindo o chrome
time.sleep(3)
pa.keyDown("command")
pa.press("space")
pa.keyUp("command")
time.sleep(1)
pa.write("chrome")
pa.press("enter")
time.sleep(1)

time.sleep(3)
# abrindo sites diários
# Email
pa.write("https://mail.google.com/mail/u/0/#inbox")
pa.press("enter")
pa.hotkey("command","t")
time.sleep(2)
# ChatGpt
pa.write("https://chat.openai.com/c/5d76b576-50da-4216-8386-1d3d401fb481")
pa.press("enter")
pa.hotkey("command", "t")
time.sleep(2)
# Youtube
pa.write("https://www.youtube.com/")
pa.press("enter")
pa.hotkey("command", "t")
time.sleep(2)
# Whatsapp
pa.write("https://web.whatsapp.com/")
pa.press("enter")
time.sleep(2)
# maxima a tela
pa.hotkey("ctrl","command", "f")

time.sleep(2)
# abrindo o vscode
pa.keyDown("command")
pa.press("space")
pa.keyUp("command")
time.sleep(1)
pa.write("visual studio code")
pa.press("enter")
time.sleep(2)
pa.hotkey("shift","command", "n")
time.sleep(2)

# abrindo pasta 
pa.hotkey("command", "o")
time.sleep(2)
pa.click(2642,380, duration=2)
pa.write("Learning_Python")
pa.click(2279,493, duration=2)
pa.click(2698,772, duration=2)

# abrindo o notion
time.sleep(2)
pa.keyDown("command")
pa.press("space")
pa.keyUp("command")
time.sleep(1)
pa.write("notion")
pa.press("enter")

