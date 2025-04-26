# crie um programa que receba do usuario uma lista de compras e ordene a lista em ordem alfabetica \n
# , apenas os nomes dos item , seu seus valores .
# faça o commit no git 

# 1 fazer toda a estrutura primeiro 
# importar bibliotecas 

import os 
#declaração da lista 
lista = []

# função do try
# ttratamento de exceção 
try:
    # loop infinit 
    while True:
     
     #input 

        item = input( "Informe o nome do item ou deixe em branco encerrar:")

  # fazer a limpeza do terminal 
        os.system ("cls") # limpa o terminal

# verifica o valor se o item esta vazio ou nao 
        if item !="":
            lista.append(item) # insere o item na lista 
            print(f"{item }  inserido com sucesso !") #mensagem de confirmação 
            continue
        else:
            break
    # ordenar a lista atravez do e saber q alista original deixa de
    #  existir lembrando que o comando sert ordena numeros de forma crecente tb 
    lista.sort()
except Exception as e:
     print(f' Não foi possivel inserir item na lista .{e}.')

finally:
     
     # fazer a ordenação colocando em oredem alfabetica que dev ser feita no try q e saida de dados 
    print("Lista de itens:\n")
    for item in lista:
        print(item)
