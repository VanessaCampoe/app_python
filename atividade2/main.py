# declarar a lista 
#lista de ciades 
# mostrar resultado correto e o errado 
# importar biblioteca 
import os
cidades = [ "Brasilia ", "Rio De Janeiro","São Paulo ",
           "Belo Horrizonte", " Goiania", "Palmas",
           "Brasilia "," Goiania", "Brasilia "
           ]
 # tratamento de exceção 
try:
 
    #loop infinito 
    while True:
        # limpeza  do terminal 
        os.system("cls") # limpA O TERMINAL 
      # usuario infoma valor a ser pesquisado 
        pesquisa = input ("Informe a cidade a ser pesquisada:").title()
        # transforma a primeira letra em maiuscula .title() não funciona para acento 
    # retorna os valores encontrados 
    # mostra o resultado na tela 
        result= cidades.count(pesquisa)
        if result != 0 :
           print(f"{pesquisa} foi encontrado na lista {result}vezes.")
        else:
            print (f" {pesquisa} não foi encontrado na lista ")
# pergunta se o usuario deseja realizar nova pesquisa 
        continuar = input ("Deseja continuar?(s/n):")
        # verifica se quer continuar 
        match continuar:
            case "s":
                continue
            case"n":
                break
            case _:
                print("Opção invalida")
                break
        
except Exception as e:
    print(f"Nâo foi realizar a busca .{e}.")












