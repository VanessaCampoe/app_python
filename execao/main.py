# tratamento de exceção em python
try:  

# declaração de varivael 
    x = int(input("informe um numero inteiro:"))

# saida de dados 
    print (f"numero informado foi {x}.")
except Exception as e:
    print (f"Não foi possivel ler o numero informado pelo usuario. {e}")
    finaly:
    print ("Meu programa foi executado com sucesso ! ")