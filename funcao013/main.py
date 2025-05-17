'''
crie um programa onde o usuario faz um cadastro de uma instituição bancaria , e opos esse cadastro o programa  exibe os seguintes menu :
0 - sair do programa 
1 - criar nova conta 
2 - alterar dados do titular da conta
3 - excluir conta
4 - fazer saque
5 - fazer deposito  
6 - consultar dados da conta 
Dados  do titular da conta 
- nome
- cpf
- agencia (1010)
- numero da conta (12345-6)
- saldo (0.00) sempre vai começar com zero


#NOTE - consulatar dados da conta envolve consultrar  saldo da conta
#NOTE - para b=numero de conta usa a biblioteca random




'''

import random

# Dicionário para armazenar as contas
contas = {}

# Função para gerar número de conta aleatório
def gerar_numero_conta():
    return f"{random.randint(10000, 99999)}-{random.randint(0, 9)}"

# Função para criar nova conta
def criar_conta():
    nome = input("Nome do titular: ")
    cpf = input("CPF do titular: ")
    numero_conta = gerar_numero_conta()
    conta = {
        'nome': nome,
        'cpf': cpf,
        'agencia': '1010',
        'numero_conta': numero_conta,
        'saldo': 0.0
    }
    contas[numero_conta] = conta
    print(f"\nConta criada com sucesso! Número da conta: {numero_conta}")

# Função para alterar dados do titular
def alterar_dados():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        nome = input("Novo nome: ")
        cpf = input("Novo CPF: ")
        contas[numero_conta]['nome'] = nome
        contas[numero_conta]['cpf'] = cpf
        print("Dados alterados com sucesso!")
    else:
        print("Conta não encontrada.")

# Função para excluir conta
def excluir_conta():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        del contas[numero_conta]
        print("Conta excluída com sucesso.")
    else:
        print("Conta não encontrada.")

# Função para fazer saque
def fazer_saque():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Valor do saque: "))
        if valor > contas[numero_conta]['saldo']:
            print("Saldo insuficiente.")
        else:
            contas[numero_conta]['saldo'] -= valor
            print("Saque realizado com sucesso.")
    else:
        print("Conta não encontrada.")

# Função para fazer depósito
def fazer_deposito():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Valor do depósito: "))
        contas[numero_conta]['saldo'] += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Conta não encontrada.")

# Função para consultar dados da conta
def consultar_dados():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        conta = contas[numero_conta]
        print("\n--- Dados da Conta ---")
        print(f"Nome: {conta['nome']}")
        print(f"CPF: {conta['cpf']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

# Menu principal
def menu():
    while True:
        print("\n--- Menu ---")
        print("0 - Sair do programa")
        print("1 - Criar nova conta")
        print("2 - Alterar dados do titular da conta")
        print("3 - Excluir conta")
        print("4 - Fazer saque")
        print("5 - Fazer depósito")
        print("6 - Consultar dados da conta")
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Saindo do programa...")
            break
        elif opcao == '1':
            criar_conta()
        elif opcao == '2':
            alterar_dados()
        elif opcao == '3':
            excluir_conta()
        elif opcao == '4':
            fazer_saque()
        elif opcao == '5':
            fazer_deposito()
        elif opcao == '6':
            consultar_dados()
        else:
            print("Opção inválida.")

# Execução do programa
menu()

        
        
        
        
        
        
