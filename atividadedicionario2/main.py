# TOTO atividade 
### 
# """
""""
Crie um CRUD, ou seja, um programa que :
  
  - cadastre
  - lista 
  - Altere   
  _Exclue
  O programa devera cadastrar pessoas com os seguintes dados:
nome, cpf , e-mail, data de nascimento , gênero
      #NOTE - : o usuario deve poder cadastrar quantas pessoas quiser,
      #NOTE - : o usuario deve fornecer um menu com as opção : cadastrar , lista , alterar , excluir , e sair do programa.

"""

import os 

lista  = [] # seu erro começõu aqui , erra pessoaas e virou lista , reveja para naao acontecer mais , faça o esquema de do fluxograma 

try:
 #TODO

    
    while True:
        usuario = {} # dicionario
        # menu interavito 
        print(f"{'='*20} CRUD COBRA {'='*20}")
        print("O que voce deseja fazer ?")
        print("\n ---Menu ---")
        print("Sair do programa ")
        print("1 - Cadastrar nova pessoa ")
        print("2 - Listar pessoas cadastradas ")
        print("3 - Alterar dados de uma pessoa")
        print("4 - Excluir pessoa")
        print("5 - Sair")
       


        opção = input("\n Informe a opção desejada: ")

        match opção:
            case "0":
              print = {"\n programa encerrado!\n"}
              break
            case "1": 
             # errro  usuario = {}             
    
          
              
                
              usuario[" nome"] = input("Digite o nome: ")
              usuario['email'] = input("Digite o email: ")
              usuario['cpf'] = input("Digite o cpf da pessoa: ") 
              usuario['telefone'] = input("Digite o telefone: ")               
              usuario['data_nascimento'] = input("Digite a data de nascimento: ")
              usuario['genero'] = input("Digite o gênero: ")


              lista.append(usuario)   # erro grave aqui viu , prestar ateção na interpretação 
              os.system ('cls' if os.name == 'nt' else 'clear')
              print(f"{usuario.get("nome") } cadastrada com sucesso!\n")
              continue


            case "2": # o segundo caso  #listar para cadastrar
              os.system ('cls' )
              for i in range(len(lista)):
                print(f"Posiçao: {i}")
                #NOTE  alterar a linha a baixo
                for chave in lista[i]:
                #NOTE  alterar a linha a baixo
                  print(f"{Chave.title()}:{ lista[i].get(chave)}")
                print("\n")
                continue  
            case "3":
              os.system("cls")
              posicao = int(input("informe a posição do usuario que deseja alterar: "))
              if lista [posicao]:
                  for chave in lista[posicao]:
                    print(f"{chave.title()}: {lista[posicao].get(chave)}")
                    print("\n")
                    dado = input("Informe o nome da chava que deseja alterar:")
                    if lista [posicao] [dado]:
                        lista [posicao] [dado] = input(f"Informe novo valor{dado}:")
                        os.system("cls")
                        print("Dados alterados com sucesso!\n")
                    else:
                        print("Chave invalida")

                  else:
                      print("Posição invalida")
                  continue
            case "4":
                  os.system("cls")
                  posicao  = int (input("Informe a posição do usuario que deseja deletar :"))
                  if lista[posicao]:
                    del(lista[posicao])
                    os.system("cls")
                    print("Usuario deletado com sucesso !")
                  else:
                      print("Não foi possivel deletar o usuario!")
                  continue


          case_:
              print("Opção invalida!")
               continue

except Exception as e:
    print(f" Não foi possivel castradar a pessoa.  {e}")             
               
               
               
               
               
               
               
               
               
               
               
               













