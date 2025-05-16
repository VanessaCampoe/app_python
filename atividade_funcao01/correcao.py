import os 
import math


def calcular_1o_grau(a, b):
    #TODO # a * x + b = 0
    x = -b/a 
    return x 
     
    
    
     
     
     
def calcular_2o_grau(a, b, c):
    if a is not 0:
        delta = (b**2) - 4*a*b
        if delta > 0:
            x1 = (- b + math.sqrt(delta))/(2*a)
            x2 = (- b - math.sqrt(delta))/(2*a)
            
            yield f"x' = {x1}"
            yield f"x'' = {x2}"
        elif delta > 0:
            x = -b/2*a
            yield f"x = {x}"
            
        else:
        
            yield  "A eqaução nao possui valores reais. "    
        
    else:
        
        yield "O valor de 'a' é zero, e por tanto não é uma equação do segundo grau."
     
    
     
     
     
if __name__=="__main__":
         
    try:
      #TODO 
      while True: 
          
          print("1 - calcular equação do 1º grau ")  
          print("2 - calcular equação do 2º grau ")  
          print("3 - Sair do programa  ")  
          opcao = input("Informe a opção desejada:")
          match opcao:
              case "1":
                  #TODO - 
                  os.system("cls")
                  a = float(input("informe o valor de 'a':").replace("," , "."))
                  b = float(input("informe o valor de 'b':").replace("," , "."))
                  result = calcular_1o_grau(a , b)
                  print(f"O valor de x em {a}x +{b} = 0 é :{result}.")
                    case "2":
                        os.system("cls")
                       
                        a = float(input("informe o valor de 'a':").replace("," , "."))
                        b = float(input("informe o valor de 'b':").replace("," , "."))
                        c = float(input("informe o valor de 'c':").replace("," , "."))
                        result = calcular_2o_grau(a , b, c)
                        for x in  result:
                            print(x)
                            
                 case "3":
                     print("Programa encerrado com sucesso.")   
                     break 
                  case _:
                          
                      print("opção invalida.")   
                      continue
    except Exception as e:
        print(f"Não foi possivel fazer o calculo.{e}.")
                       
                       
                       
                       
          
          
          
          
          
          
          
          
          
          
          
          
          