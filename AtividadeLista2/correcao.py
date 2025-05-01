notas = []

nome = input("Digite o nome do aluno: ")

while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip()
    
    if entrada.lower() == "fim":
        break

    try:
        nota = float(entrada.replace(",", "."))
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número válido ou 'fim' para encerrar.")

# Verifica se foram inseridas notas
if notas:
    media = sum(notas) / len(notas)
    print(f"\nA média de notas do aluno {nome} é {media:.2f}.")

    if media >= 7:
        print(f"Olá {nome}, você foi APROVADO.")
    elif media >= 5:
        print(f"Olá {nome}, você está em RECUPERAÇÃO.")
    else:
        print(f"Olá {nome}, você foi REPROVADO.")
else:
    print("Nenhuma nota foi inserida.")
