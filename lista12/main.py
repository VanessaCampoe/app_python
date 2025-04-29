nomes = ["Fulano", "Ciclano", "Beltrano", "Joao", "Maria", "José"]

try:
    for i in range(len(nomes)):
        print(f"codigo {i}: {nomes [i]}.")
    posicao = int (input("Informe o codigo do nome a ser separado: "))
    nome_separado = nomes.pop(posicao) # separa o nome da lista
    os.system ("cls")
    print(nome_separado)
except Exception as e:
    print(f" Não foi possivel sepaaro item da lista .{e}.")





    # aqui vou fazer so uma separação sem o loop infinito e vou encerrrar o programa 
    # função do .pop() e separar o nome da lista
    # e colocar em uma variavel
    # comando salvador de vidas 
    # fazer um crud inserir pesquisa deletar buscar por crud e tb no dicionario 
    # lista 13 jeson