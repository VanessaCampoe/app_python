# adicionar um nova chave a um dicionario que ja foi criado
# o usuaio vai acrecentar um dao a mais nesse dicionario 
import os
dados = {
    'nome': 'Alex Machado',
    'idade': 40,
    'email': '000.000.000.00'  
    
}

# exibir dados dicionario
for chave in dados:
    print(f'{chave.title()}: {dados.get(chave)}')
    
    # vamos sair daqui pq esta mostrando dados e não é isso que queremos queremos inserir dados
dados['email'] = input("\nDigite o seu email do usuario : ")

os.system('cls') 
for chave in dados:
    print(f'{chave.title()}: {dados.get(chave)}')
    