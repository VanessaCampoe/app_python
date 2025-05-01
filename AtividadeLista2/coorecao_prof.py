import os
notas = []   






try:
    while True:
        nota = float(input(" Digite a nota do aluno : ").replace(",", "."))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            print (f" nota inserida com sucesso !")
            while True:
                continuar = input("Deseja inserir outra nota ? (s/n) : ")
                if continuar ==  "s" or continuar == "n":
                    os.systen("cls")
                    break
                else:
                    print("opcao invalida")
                    continue
            match continuar:
                case "s":
                    continue
                case "n":
                    break
        else:
            print(f"nota invalida . favor diigiitar uma nota valida.   ")
    for i in range (len(notas)):
        print (f" a nota {i} é {notas[i]}")

    media = sum(notas)/len(notas)
        
except Exception as e:
    print (f" nao foi posivel inserior as notas e calcular a media {e}.")
finally:
    print(f"\nMedia do aluno  é {media:,.2f}.")
    if media >= 7:
        print(f"O aluno esta aprovado. ")
    elif media >= 5:
        print(f"O aluno esta em recuperacao.")
    else:
        print(f"O aluno esta aptovado.")







  