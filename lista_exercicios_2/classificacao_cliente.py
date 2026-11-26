nome_cliente = input("Digite seu nome: ")

total_compras_mes = float(input("Valor total de compras no mês: "))

if total_compras_mes >= 5000:
    print("Cliente Ouro! ")

elif total_compras_mes >= 2000:
    print("Cliente Prata! ")

else:
    print("Cliente Bronze! ")

