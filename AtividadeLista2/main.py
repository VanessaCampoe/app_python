'''
criew um programa em que o usurario informa varias notas  de uma aluno de 0 a 10
(quantas notas ele quiser inserir ) e ao final , o programa  calcula a media desse aluno
 e informe se ele está aprovado ou reprovado .
 obs:media para aprovação : 7 media recuperação : 5 a 7 . Abaixo reprovado .
'''
# buscar como mudar o ponto e a virgula no python
"""
numero_decimal = float(input("Informe um numero decimal: ").replace(",", "."))
print (f"{numero_decimal}, {type(numero_decimal)}") 
"""

#.replace(",", ".") # troca a virgula pelo ponto
 

nome = input(" Digite o nome do aluno : ")
nota1 = float(input(" Digite a nota do aluno : ")).replace(",", ".")
nota2 = float(input(" Digite a nota do aluno : ")).replace(",", ".")
nota3 = float(input(" Digite a nota do aluno : ")).replace(",", ".")
nota4 = float(input(" Digite a nota do aluno : ")).replace(",", ".")
media = (nota1 + nota2 + nota3 + nota4) / 4 # media aritmetica

print (f" a média de nota do aluno {nome} é {media}.")

if nota >= 0 and nota <= 10: #definine o parametro a ser seguido , desse ponto a esse ponto e pronto, caso ao contrario ela da como invalido.
    if nota >= 7:
        print(f"Olá {nome}, você foi APROVADO com a nota {nota}.")
    elif nota >= 5:
        print(f"Olá {nome}, você está em RECUPERAÇÃO com a nota {nota}.")
    else:
        print(f"Olá {nome}, você foi REPROVADO com a nota {nota}.")
else:
    print(f"Olá {nome}, a nota {nota} é inválida. A nota deve ser entre 0 e 10.")















