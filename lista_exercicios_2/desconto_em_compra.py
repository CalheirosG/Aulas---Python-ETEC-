valor_compra = float(input("Digite o valor total da compra do cliente: "))

if valor_compra >= 500:
    desconto = valor_compra * 0.10

    print(f"Parabéns, você recebeu um desconto de 10%.\nValor original da compra: R${valor_compra:.2f}\nValor com desconto: R${valor_compra-desconto:.2f}")

else:
    print(f"Não se aplica. faltam R${500-valor_compra:.2f} para atingir o desconto de 10%. ")
    print(f"O valor total da sua compra é de: R${valor_compra:.2f}")
