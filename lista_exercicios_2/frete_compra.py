valor_compra = int(input("Digite o valor total da compra: "))
frete = 0


if valor_compra <= 300:
    frete = 25

print(f"O valor final do seu pedido é de R${valor_compra+frete:.2f} ")
