
# repetição de algoritmo

try:
    while True:
        # declaração de variáveis
        nome = input("informe seu nome:")
        idade = int(input("informe sua idade:"))

        # saída de dados
        print(nome, "é maior de idade." if idade >= 18 else "é menor de idade.")

        # decisão
        continuar = input("deseja continuar (s/n):")

        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("não foi possível computar sua decisão.")
                continue

except Exception as e:
    print(f'Dados informados inválidos: {e}.')

# tratamento de exceção em python
finally:
    print("Programa finalizado com sucesso!")