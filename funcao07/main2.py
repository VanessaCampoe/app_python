''' Crie um programa que calcule um numero informado pelo usuario DA SEQUENCIA  fibonacci .
utilize a função recursiva 
'''

def calcular_fibonacci(n):
    return n if n <= 1 else calcular_fibonacci(n-1) + calcular_fibonacci(n-2)
if __name__ == "__main__": 
    try:
        n = int(input("Informe um número em sequencia desejada: "))
        #result = calcular_fibonacci(n)         
         
         
         
            
        #print(f"O número {n} na sequencia de fibonacci é: {result}")
        for i in range(1, n+1): 
            print(calcular_fibonacci(i))

    except Exception as e:
        print(f"Não foi possivel calcular a sequencia de fibonacci. {e}.")
        
            








