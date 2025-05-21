# ativiade 
'''
crie um programa que comita  o projeto de vc e envie o repositorio para o git 

'''

import pyautogui as auto

auto.hotkey('ctrl', 'shift', 'p')
auto.typewrite('Git: Commit')
auto.press('enter')
auto.typewrite('Atualizando o projeto')
auto.press('enter')
auto.hotkey('ctrl', 'shift', 'p')
auto.typewrite('Git: Push')
auto.press('enter')
