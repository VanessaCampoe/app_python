# edclaração  de dicionario 
#usar aspas simples para dicionario
usuario = {''
'nome' : "Alex Machado",
'idade': 40 ,
'profissao': "Programador"

}

# espas duplas ai pq ?
'''   print(f"Nome:{usuario['nome']}")
    print(f"Idade:{usuario["idade"]}") 
    print (f"Profissição:{usuario['profissao']}") 

'''
# exibir os dados do  dicionario
print(f"Nome:{usuario.get('nome')}")
print(f"Idade:{usuario.get('idade')}")
print(f"Profissição:{usuario.get('profissao')}")
print(f"Cpf:{usuario.get('Cpf')}")




















#decelarizar dicionario