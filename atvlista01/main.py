# crie um programa que receba do usuario uma lista de compras e ordene a lista em ordem alfabetica \n
# , apenas os nomes dos item , seu seus valores .
# faça o commit no git 

# declarar a lista  
compra = []

# tratamento de exceção 
try:
    # loop infinito 
    while True:
    ## usuario infoma nome 
        produtos = input("Informe um nome ou deixe-o em branco para exibir a lista :")




# verificar se o nome foi inserido 
        if produtos != "":
            compra.append(produtos)
            continue
        else:
            break

# ordem alfabetica
    compra.sort()        

except Exception as e:
    print(f" Não for possivel inserir produtos na lista .{e}.")

finally:
    for produtos in compra:
        print(produtos)









