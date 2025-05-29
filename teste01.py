import pyautogui
import time

# Esperar um momento para garantir que o Paint esteja aberto e pronto
time.sleep(5)

# Mover o mouse para a posição inicial do círculo
pyautogui.moveTo(100, 100)

# Desenhar o círculo
pyautogui.mouseDown()
pyautogui.moveTo(200, 100)
pyautogui.mouseUp()

# Esperar um momento para garantir que o círculo foi desenhado
time.sleep(1)
