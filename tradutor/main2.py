from deep_translator import GoogleTranslator

try:
    # instancia objto traduto 
    
    tradutor = GoogleTranslator(source='auto', target="pt")       # instancia de uma classe orientação ao obejto construtor q recebe 2 paramentros

    while True:
        # entrada de dados
        texto_original = input(" Digite um texto a ser tradzido em qualquer idioma : ")
        # chamada de um método da classe tradutor       
        texto_traduzido = tradutor.translate(texto_original)
        
        print(f'Texto traduzido: "{ texto_traduzido}"\n') 
        encerrar = input("Deseja encerrar o programa? (S/N)")
        
        match encerrar:
            case"S":
                continue 
            case"N":
                break
            case _: 
                print("Opção inválida!")
          
except Exception as e: 
    print(f"não foi possível traduzir o texto: {e}") # exibe o resultado da tradução

