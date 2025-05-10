# lista dentro do dicionario 

pessoas = [
        {
    "nome": "Fulano de tal",
    "idade": 18,
    "email": "fulando@gamil.com"
    },
        {

    "nome": "Ciclano de tal",
    "idade": 25,
    "email": "ciclano@gmail.com"        
    },
        {
    "nome": "Beltrano de tal",
    "idade": 30,
    "email": "beltrano@gmail.com"

    }
]

for pessoa in pessoas:
    print(f"\n{"-"*20}\n")
    for chave in pessoa:
        print(f"{chave.title()}: {pessoa.get(chave)}.")
    
    
# se erro mais uma vez foi a identação , precisa fazer a estrutura da identação 