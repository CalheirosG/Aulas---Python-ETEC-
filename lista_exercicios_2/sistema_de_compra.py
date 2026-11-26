nome_cliente = input("Digite o nome do cliente: ")
nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Preço unitário: "))
quantidade = int(input("Quantidade: "))

valor_total = preco_unitario * quantidade
valor_desconto = 0

if valor_total >= 1000:
    percentual_desconto = 15
    valor_desconto = valor_total * percentual_desconto / 100

elif valor_total >= 500:
    percentual_desconto = 10
    valor_desconto = valor_total * percentual_desconto / 100

elif valor_total > 200:
    percentual_desconto = 5
    valor_desconto = valor_total * percentual_desconto / 100

else:
    percentual_desconto = 0
    valor_desconto = 0

total_a_pagar = valor_total - valor_desconto

print(f"""
Nome do cliente: {nome_cliente}
Subtotal: {valor_total:.2f}
Percentual de desconto: {percentual_desconto}% 
Valor do desconto: {valor_desconto:.2f}
Total a pagar: R${total_a_pagar:.2f} """)
