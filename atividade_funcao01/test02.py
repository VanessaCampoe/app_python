# função que calcula a equação do 1º grau
'''
crie um porgramaonde o usuario pode escolher se deseja calcular a equação do 1º
grau ou a equação do 2ª grau , e o programa retorna o resultado da e equação 

'''
# NOTE O programa deverá ser executado em loop  
def calcular_equacao_primeiro_grau( a , b  ):
    x = -b/a
    return x

# programa principal
a = int(input('Informe o valor de "a": '))
b = int(input('Informe o valor de "b": '))
c = int(input('Informe o valo de "c": '))
print(f'O valor de "x" na equação do 1º grau é {calcular_equacao_primeiro_grau(a, b)}.')
print(f'O valor de "x" na equação do 2º grau é {calcular_equacao_primeiro_grau(a, b, c)}.')

decisao = input("resolva uma equação ") 

match decisao:
    case '1':
        a = int(input('Informe o valor de "a": '))
        b = int(input('Informe o valor de "b": '))
        
        
 
    case '2':
        a = int(input('Informe o valor de "a": '))
        b = int(input('Informe o valor de "b": '))
        c = int(input('Informe o valor de "c": '))
        pass
    case _:
        print('Resposta inválida!')