import pyautogui as p 

def limpar_credenciais():
   
    p.write("git config --global user.name ")
    p.press("enter")
    p.write("git config --global user.email ")
    p.press("enter")

if __name__ == "__main__":

    p.PAUSE = 0.5

    msg_commit = input("Infome a mensagem deo commit") # aqui vou ter que colocar na hora / fazer para minha senha , o que nao quero , vou aprender de outro jeito inferno


#p.hotkey("ctrl", "j")

limpar_credenciais()


p.write ("git config --global user.name 'VanessaCampoe'")
p.press("enter")
p.write ("git config --global user.email 'vanessacampoe2@gmail.com'")
p.press("enter")
p.write("git add .")
p.press("enter")
p.write(f"git commit -m '{msg_commit}'")
p.press("enter")
p.write("git push")
p.press("enter")

limpar_credenciais()










