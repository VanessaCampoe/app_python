from deep_translator import GoogleTranslator

# declaração de variáveis # estancia de uma classe orientação ao obejto construtor q recebe 2 paramentros 
tradutor = GoogleTranslator(source='auto', target="pt")       # instancia de uma classe orientação ao obejto construtor q recebe 2 paramentros
texto_original = input(" Digite um texto a ser tradzido em qualquer idioma : ") # entrada de dados
texto_traduzido = tradutor.translate(texto_original) # chamada de um método da classe tradutor


# exibe o texto traduzido 
print(f"Texto traduzido: "{ texto_traduzido}"")    # exibe o resultado da tradução



