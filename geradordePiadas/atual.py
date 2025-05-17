# importa bibliotecas
import pyjokes
from deep_translator import GoogleTranslator

while True:
    # gera piada em inglês
    piada = pyjokes.get_joke()
    
    # traduz para português
    piada_traduzida = GoogleTranslator(source='auto', target='pt').translate(piada)

    # exibe piada traduzida
    print(piada_traduzida)

    repetir = input('Gerar outra piada? "s" para sim; qualquer outro valor para encerrar: ').lower()
    if repetir != 's':
        break











