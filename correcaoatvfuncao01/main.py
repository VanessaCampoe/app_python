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
import os 
import random
import modulo as m


if __name__ == "__main__":
    titular = {}
    try:
        while True:
            
                print(f"{'=' * 30} Banco cobra {'=' * 30}")
                print(' 0 sai do programa ')
                print(' 1 criar nova conta ')
                print(' 2 alterar dados do titular da conta ')  
              #  print(' 3 excluir conta ')
                print(' 3 fazer saque ')
                print(' 4 fazer deposito ')
                print(' 5 consultar dados da conta ')
               # print = input('Digite a opção desejada: ')
                os.system('cls')
        match opcao:
                case '0':
                    print('Programa encerrado com sucesso.')
                    print('Tenha um otimo dia !')
                    break
                case '1':
                    titular = ["agencia"] = 1010
                    titular["num_conta"] = r.randint(10000, 99999)
                    titular["saldo"] = 0.00
                    titular["nome"] = input('Digite o nome do titular: ')
                    titular["cpf"] = input('Digite o CPF do titular: ')
                   
                    os.system('cls')
                    print(f'Conta {titular("num_conta")} criada com sucesso!\n')
                    continue

                case '2':
                    print(f"Nome: {titular.get['nome']}")
                    print(f"CPF: {titular.get['cpf']}\n")
                    campo = input ('Digite o campo que deseja alterar:').strip().lower()
                    match campo:
                        case 'nome':
                            titular["nome"] = input('Informe o novo nome do titular: ')
                            os.system('cls')
                            print(f'O nome do titular foi atualizado com sucesso.')
                        case 'cpf':
                            titular["cpf"] = input('Informe o novo CPF do titular: ')
                            os.system('cls')
                            print(f'O CPF do titular foi atualizado com sucesso.')
                        case _:
                          print('Campo inválido.')
                             
                             
                     continue
                case'3':
                    valor = float(input('Informe o valor do saque: R$ ')).replace(',', '.')
                    saldo = titular.get("saldo")    
                    if valor > salado :
                        titular["saldo"] = m.fazer_saque (saldo , valor )
                        os.system('cls')
                        print('Saque efetuado com sucesso!')
                    else:
                        print(f" Nao foi possivel efetuar o saque . Valor insidsponivel ")
                      
                case "4":
                          valor = float(input('Infome o valor do desposito : R$ ')).replace(',', '.')
                          titular["saldo"] = m.fazer_deposito(titular["saldo"], valor) 
                          os .system ("cls ")
                          print ("Deposito efetuado com sucesso !")
                          print (f"Seu saldo atual é de R$ {titular['saldo']:.2f}")
                          continue
                case "5":
                          m.consultar_dados(titular)
                          os.system('cls')
                          print(f"Seu saldo atual é de R$ {titular['saldo']:.2f}")
                          continue
                case _:
                    print('Opção inválida. Tente novamente.')
                    continue


except Exception as e:
    print(f"Ocorreu um erro: {e}")

                    