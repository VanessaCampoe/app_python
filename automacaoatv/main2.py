
'''
crie um programa que comita  o projeto de vc e envie o repositorio para o git 

'''
import pyautogui as auto


auto.PAUSE = 0.5
auto.press("win")
auto.write("firefox")
auto.press("enter")
auto.hotkey("alt", "space")
auto.press("x")
auto.write("https://github.com/login/") #foco na procima para ir direto no endereço de login

auto.write("tab ate Sign in ")
auto.press("enter")
auto.write("vanessacampoe2@gmail.com")  
auto.press("tab")
auto.write("a258700921")  
auto.press("enter")
auto.hotkey("ctrl", "l")  # Focar na barra de endereços
auto.write("https://github.com/VanessaCampoe/app_python")   
auto.press("enter")
auto.press("win")
auto.write("vscode")
auto.press("enter")
auto.press("ctrl", "j")
