# note : o split separa os valores de uma string e coloca em uma lista
# variavel 
ano = "jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez"
# algoritimo 
try:
    # TODO
    ...


    meses = ano.split(", ") # separa os valores da string e coloca em uma lista
    for mes in meses:
        print(mes) 

except Exception as e:
     print(f" não foi possivel separar os valores. {e}.")
    

    # no anterior eu podia escolher o delimitador aqui eu não posso
    # o delimitador e a virgula e o espaco  
    # o split separa os valores de uma string e coloca em uma lista
    