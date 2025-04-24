# declarar a lista  
nomes = []

# tratamento de exceção 
try:
    # loop infinito 
    while True:
    ## usuario infoma nome 
        item = input("Informe um nome ou deixe-o em branco para exibir a lista :")




# verificar se o nome foi inserido 
        if item != "":
            nomes.append(item)
            continue
        else:
            break

# ordem alfabetica
    nomes.sort()        

except Exception as e:
    print(f" Não fo possivel inserir dados na lista .{e}.")

finally:
    for item in nomes:
        print(item)


    #TODO - 