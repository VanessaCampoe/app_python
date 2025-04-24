#tratamento de exeções 
try:
    # declaração de variaveis 
    n = int(input("informe um numero inteiro positivo:"))

    #loop 
    while n >= 0:
        print(n)
        n -= 1

except Exception as e:
    print(f'Numero invalido: {e}.')
