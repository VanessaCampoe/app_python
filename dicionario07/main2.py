# deletar a chave 
import os 
chaves= ("nome", "idade", "cpf", "telefone", "email","profissão")
usuario = {
    chaves[0]: " Alex Machado",
    chaves[1]: 40,
    chaves[2]: "123.456.789-00",
    chaves[3]: "123456789",
    chaves[4]: "Alex@gmail.com",
    chaves[5]: "Programador"
}
try:
    while True:
        # eliminar esse comando dessa linha :     os.system("cls")
        for chave in usuario:
            print(f"{chave.title()}: {usuario.get(chave)}")
        prosseguir = input("Deseja excluir alguma chave ? (s/n):")
        match prosseguir:
                case "s":
                    chave_escolhida = input("Informe o nome da chave que deseja excluir:")
                    if chave_escolhida in chaves:
                        usuario.pop("", None)
                        # usuario[chave_escolhida] = input(f"Informe o novo valor para a chave {chave_escolhida}: ") 
                        os.system("cls")
                        continue
                    else:
                        os.system("cls")
                        print(f"{chave_escolhida} não existe")
                        continue
                case "n":
                    break
                case _:
                    print("Opção inválida.")   
                    continue  
       
except Exception as e:
    print(f"Não foi possivel atualizaros dados.{e}.")        
         
         
         
         
         
         
         
         
         
         