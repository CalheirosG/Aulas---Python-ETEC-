valor_compra = float(input("Digite o valor da compra: "))
forma_pagamento = int(input("""Digite qual será a forma de pagamento: 
[1] - PIX
[2] - Dinheiro
[3] - Cartão
:"""))

desconto = 0

if forma_pagamento == 1:
    desconto = valor_compra * 10 / 100

elif forma_pagamento == 2:
    desconto = valor_compra * 5 / 100

elif forma_pagamento == 3:
    pass

else:
    print("Opção inválida, desconto não aplicado. ")

valor_final = valor_compra - desconto

print(f"O valor final da sua compra é de: R${valor_final:.2f}")
