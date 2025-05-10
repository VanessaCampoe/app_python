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
pessoas = []
try:
 #TODO

    
    while True:
        # menu interavito 
        print("\n ---Menu ---")
        print("1 - Cadastrar nova pessoa ")
        print("2 - Listar pessoas cadastradas ")
        print("3 - Alterar dados de uma pessoa")
        print("4 - Excluir pessoa")
        print("5 - Sair")
        opção = input("Escolha uma opção: (1-5): ")
        match opção:
            case "1":
               pessoa = {}
               
               
    match cadastrar:
            case "s":
                pessoa = {}
                
                pessoa[" nome"] = input("Digite o nome: ")
                pessoa['email'] = input("Digite o email: ")
                pessoa['cpf'] = input("Digite o cpf da pessoa: ")
                
                pessoa['data_nascimento'] = input("Digite a data de nascimento: ")
                pessoa['genero'] = input("Digite o gênero: ")
                pessoas.append(pessoa)             
               
               
               
               
               
except Exception as e:
    print(f" Não foi possivel castradar a pessoa.  {e}")             
               
               
               
               
               
               
               
               
               
               
               
               













