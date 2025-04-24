x =float(input("informeo valor de x"))
y =float(input("informeo valor de y"))

print ("escolha a operação desejada :")
print ("1 - soma")
print ("2 - subtração")     
print ("3 - multiplicação")
print ("4 - divisão")
print ("5 - resto da divisão")
operador = input("escolha a operação desejada: ")

# estrutura match para calcular a operação desejada

match operador: 
    case "1":
        print(f"Resultado da soma:{x+y}.") 
    case "2":
        print(f"Resultado da subtração:{x-y}.")      
    case "3":
        print(f"Resultado da multiplicação:{x*y}.")
    case "4":
        print(f"Resultado da divisão:{x/y}.")
    case "5":
        print(f"Resultado do resto da divisão:{x%y}.")

    case _:
        print ("operação inválida")
