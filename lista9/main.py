# importação de bibliotecas
import os 

nomes = ["Fulano", "Ciclano", "Beltrano", "Zezinho", "Maria", "Ana", "João"]
# tratamento de exceção 
try:
    while True:

        #limpa o terminal


        #os.system("cls") # limpa o terminal tirei fora 
        #exibir a lista
        for i in range(len(nomes)):
            print(f"Nome de codigo {i}: {nomes [i]}.")
        opcao = input("Deseja exclui o itm da lista ? (s/n):")
        match opcao:
            case "s": 
                posicao = int(input("Informe o codigo do nome a ser alterado"))
                del nomes[posicao]
                os.system("cls") 
                print(f"Nome {nomes[i]} foi excluido com sucesso.")
                continue
            case "n":
                break
                
            case _:
                print("Opção invalida")
                
                continue

except Exception as e:
     print(f" Não fo possivel inserir dados na lista .{e}.")
