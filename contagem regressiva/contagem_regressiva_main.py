# import biblioteacas
import time
import os 


# tratamento de eceção 


try: 
# todo

    n = int(input('informe um numero inteiro posisitivo :'))

# laço de repetição 
    for n in range (n,-1, -1 ):
        os.system("cls")
        print(f'{n}...')
        time.sleep(1)
    
    print ("BOMMMMM!!!")
    print(" A cobra explodiu !!")
    
except Exception as e :
    print(f"Não foi possivel realizar a contage regressiva.{e}.")
