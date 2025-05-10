# correção 
#TODO

#crie um programa que inicialise um dicionario zerado,
# e o usuario adicione e inserir os seguintes dasos:
# nome , data de nascimento, idade, cpf, e-mail, genero , telefone , altura, peso, 
# tipo sanguineo,  e no final o programa deve imprimir todos os dados do usuario e seu imc.
# note o usaurio devera inserir apenas os valores dessas chaves,
# note  o programa devere exibir os daods em linhas diferentes 
usuario = {}
try:
    
    usuario["nome"]= input( "Informe o nome:")
    usuario["data de nacimento" ] = input(" Informe a data de nascimento :")
    usuario["cpf"] = input("informe p cpf :")
    usuario["e-mail"] = input(" Informe o e-mail")
    usuario["genero"] = input(" Informe o genero ")
    usuario["telefone "] = input(" Informe telefone")
    usuario["altura"] = input(" Informe o altura").replace(",",".")
    usuario["peso"] = input(" Informe o peso ").replace(",",".")
    usuario["Tipo sanguineo "] = input(" Informe o Tipo sanguineo ")

    for chave in usuario:
        print(f"{chave.title()}: {usuario.get(chave)} ")
        
    imc = usuario.get('peso')/usuario.get('altura')**2

    print(f"imc de {usuario.get('nome')}: {imc:,.2f}")

    if imc <= 18.5:
        print (f"{usuario.get('nome')} esta a baixo do peso  ")

    elif imc <= 25:
        print(f"{usuario.get('nome')} esta no peso ideal, Parabens ")
    elif imc <= 30:
        print (f"{usuario.get('nome')} esta  acima do peso ideal ")
    elif imc <= 35:
        print (f"{usuario.get('nome')} esta  obeso  ")
    elif imc <= 40:
        print (f"{usuario.get('nome')} esta com obesidade tipo II")
    else:
        print (f"{usuario.get('nome')} esta com obesidade morbida. Procure um medico !!!")
except Exception as e:
    print(f"Não fo possivel inserir os dados.{e}. ")
    









