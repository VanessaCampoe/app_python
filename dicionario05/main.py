chaves= ("nome", "idade", "cpf", "telefone", "email","profissão")
usuario = {
    chaves[0]: " Alex Machado",
    chaves[1]: 40,
    chaves[2]: "123.456.789-00",
    chaves[3]: "123456789",
    chaves[4]: "Alex@gmail.com",
    chaves[5]: "Programador"
}
for chave in usuario :
    print(f"{chave.title()}: {usuario.get(chave)}")
    