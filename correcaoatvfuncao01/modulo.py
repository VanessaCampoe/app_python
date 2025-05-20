def fazer_deposito (saldo, valor):
    saldo += valor
    return saldo
 
def fazer_saque (saldo, valor):  # observe os sinais , quanto acrescenta ou diminui o valor da conta bancaria 
    saldo -= valor
    return saldo


def consultar_dados(titular):
    print("{"-"*20} Dados da Conta {"-"*20}\n")
    print(f"Nome: {titular.get('nome')}")
    print(f"CPF: {titular.get('cpf')}")
    print(f"Agência do titular : {titular.get('agencia')}")
    print(f"Número da Conta: {titular.get('num_conta')}")
    print(f"Saldo da conta do titular : R$ {titular.get('saldo'):.2f}")
    print("{"-"*20} Dados da Conta {"-"*20}\n")
          

