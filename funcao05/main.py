 # importar modulo 
 
from funcoes import calcular_quadrilatero, calcular_triangulo


if __name__ == "__main__":
    
    try:
        
        
        print("Escolha a figura de qual deseja calcular a área: \n")
        print("1 - Quadrilatero ")
        print("2- triangulo")
        opcao = input("Opcao desejada: ")
        if opcao == "1" or opcao == "2":
            b = float (input("informe o valor da base:").replace("," , "."))
            h = float (input("informe o valor da altura:").replace("," , ".")) 
            match opcao:
                case" 1" :
                    resultado = calcular_quadrilatero (b, h)
                    print(f"Area do quadrilatero :{ resultado }")
            
                case" 2":
                    resultado = calcular_triangulo (b, h)
                    print(f"Area do triangulo :{ resultado }")
        else:
            print ("opcao inavalida . Proprama encerrado!")
            
        
        #uadrilatero = funcoes.calcular_quadrilatero (b, h)
        
       #print(f"A área do quadrilatero é {quadrilatero}.")
        
         
    except Exception as e :
        print(f"Não foipossivel executar a operação.{e}.")
        

# pode acontece de gerar uma pasta com__pycache__ nao se preocupe com ela 













