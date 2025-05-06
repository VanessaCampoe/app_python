#TODO

#crie um programa que inicialise um dicionario zerado,
# e o usuario adicione e inserir os seguintes dasos:
# nome , data de nascimento, idade, cpf, e-mail, genero , telefone , altura, peso, 
# tipo sanguineo,  e no final o programa deve imprimir todos os dados do usuario e seu imc.
# note o usaurio devera inserir apenas os valores dessas chaves,
# note  o programa devere exibir os daods em linhas diferentes 

import os 

dados = {
    'nome': 'Ana',
    'data_nascimento': '10/02/2000',
    'idade': 40,
   
}
cpf = input("Informe o seu CPF: ")
e_mail = input("Informe o seu e-mail: ")
genero = input("Informe o seu genero: ")
telefone = input("Informe o seu telefone: ")

altura = input("Informe a sua altura: ")
peso = input("Informe o seu peso: ")
tipo_sanguineo = input("Informe o seu tipo sanguineo: ")
imc = float(peso) / (float(altura) ** 2)
print(f"Atualização do usuario \n{dados} a seguir são: \n{cpf}, \n{e_mail}@gmail.com, \n {genero},\n{telefone}, \n{altura}, \n{peso}, \n{tipo_sanguineo}. \nSeu imac é:{imc}")














