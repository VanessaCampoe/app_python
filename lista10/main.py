#lista join note : e um comando que pega os valores de uma lista  
# junta em uma unica variavel 

dias = [ 
    "Domingo-feira ",
    "Segunda-feira ", 
    "Terça-feira", 
    "Quarta-feira", 
    "Quinta-feira", 
    "Sexta-feira", 
    "Sabado"
         ]
# juntar os nomes em um unic valor 
# e colocar em uma variavel vaai ser um separador 

separador = ", " # delimitador
semana = separador.join(dias) # junta os itens/ valores da lista em uma string

# exibe na tela 
print(semana)



# erro na excusao limpar e fechar os terminais no lixinho não so a limpeza do terminal nao funciona 