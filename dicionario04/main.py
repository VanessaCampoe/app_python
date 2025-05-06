import os 
dados = {
    'nome': 'Alex Machado',
    'idade': 40,
    'cpf': '000.000.000-00',
    
}
try :
    while True:
        os.system('cls')
        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}")
            # usuario infoma se deseja inserir um novo chave ou encerrar 
            prosseguir = input("\nDeseja inserir novos dados? (s/n): ")
            
            match prosseguir:
                case 's':
                    # usuario informa o nome da nova chave e o valor da nova chave 
                    # e o programa insere no dicionario 
                    nova_chave = input ('\nInforme o nome da nova chave: ')
                    # aqui tem q pedir para incluuir 
                    #ou sej dados nova chave 
                    # cahmar o novo dicionario 
                    dados[nova_chave] = input (f'Informe o valor da {nova_chave}: ')
                    continue
                case 'n':
                    break
                case _:
                    print("Opção inválida. ")
                    continue
    
except Exception as e:
    print(f"Não foi possivel inserir a nova chave: {e}.")
    
    
    
    
    # nome do jogo while True:learn()