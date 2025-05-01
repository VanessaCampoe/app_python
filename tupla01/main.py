# tuplas 
dias_semana = ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado")
# tuplas trabalha com parentes se vc ver uma tupla saiba que e com parenteze
#ser tiver parecentes vai ser tupla 

# lista tupla 
for dia in dias_semana:
    print(dia)


try:

    # tentativa de fazer operação de lista 
    dias_semana.append("Setima" )


    print ("\n")

    for dia in dias_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possivel inserir item na tupla {e},")


# para fazer a pesquisa atravez da tupla ....