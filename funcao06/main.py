import time 
import modulo as m 

if __name__ =="__main__":
    nome = input("Informe o nome do aluno: ")
    
    
    
    resultado  = m.verificar_matricula(nome)  # como ele recebe varios valores ele precisa ser exbido como uma lista 
    

    for verificacao in resultado :
        time.sleep(3)
        print(verificacao)
        








