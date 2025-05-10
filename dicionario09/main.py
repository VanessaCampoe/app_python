import os 

pessoas = []

try:
 #TODO

    
    while True:
        cadastrar = input("Deseja cadastrar uma nova pessoa? (s/n): ")
        match cadastrar:
            case "s":
                pessoa = {}
                
                pessoa[" nome"] = input("Digite o nome: ")
                pessoa['email'] = input("Digite o email: ")
                pessoa['cpf'] = input("Digite o cpf da pessoa: ")
                
                pessoas.append(pessoa)
                
                os.system('cls')
                print(f'{pessoa.get('nome')}cadastrado com sucesso!')                
                for pessoa in pessoas:
                    print(f"\n{"-"*20}\n")
                for chave in pessoa:
                    print(f"{chave.title()}: {pessoa.get(chave)}.")
                continue
            case "n":
                break
            case _:
                print("Opção invalida.")
    
except Exception as e:
    print(f" Não foi possivel castradar a pessoa.  {e}")  