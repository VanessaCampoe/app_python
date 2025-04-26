# importar bilbioteca 
import os 
# declaração de varival 
cidades = [ "Brasilia ", "Rio De Janeiro","São Paulo", "Curitiba", "Fortaleza"]
#
# tratamento de exceção 
try:
  # loop infinito
    while True:
        # exibe a lista de cidades
        for i in range(len(cidades)):
            print(f"Cidades de codigos {i} : {cidades[i]}.")
            # usuario informa se deseja alterar algum valor
        alterar = input("Deseja alterar alguma valor?(s/n):")
        match alterar:
            case "s":
                        # usuario informa posição do valor q deseja ser alterado
                codigo_cidade = int(input("\n Informe o codigo da cidade que deseja mudar:"))
                nova_cidade = input("Informe o nome da nova cidade:") # usuario informa o novo valor 
                cidades[codigo_cidade] = nova_cidade #troca de valor
                os.system("cls") # limpa o terminal
                continue
            case "n":
                break
            case _:
                print("Opção invalida")
                break
         
except Exception as e:
    print(f"Não foi possível exibir a lista.{e}.")


     