#lamida em python 

import math
# funçaõ normal
#def calcular_carea_circula(r):
   # area = math.pi * (r ** 2)
  #  return area
  
  
calcular_carea_circula = lambda r: math.pi * r**2
if __name__ == "__main__":
    try:
        r = float(input("Informe o raio do circulo: "))
        result = calcular_carea_circula(r)
        
        
        
        print(f"A area do circulo é: {result}")
    except Exception as e:
        print(f"Não foi possivel calcular a area do circulo. {e}.")
 










