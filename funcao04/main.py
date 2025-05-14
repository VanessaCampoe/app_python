# declaração de função 
def calcular_triangulo (d, h):
    area = (d*h)/2
    return area

try:
    b = float(input("Infrome o valor da base :").replace(',' , '.'))
    h = float(input("Infrome o valor da altura :").replace(',' , '.'))
    area = calcular_triangulo (b,h)
    
    print(f"O valor da area do triangular é {area}.")
except Exception as e:
     print(f"Não foi possivel calcular")














