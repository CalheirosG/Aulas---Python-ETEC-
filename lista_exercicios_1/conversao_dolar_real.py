dolar = input("Digite a quantidade em dólar que você deseja converter para R$: ")
cotacao_dolar = float(input("Digite a cotação atual do dólar: "))

conversao = dolar * cotacao_dolar

print(f"O valor de {dolar} convertido para R$ é r${conversao:.2f}")

