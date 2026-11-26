fornecedor1 = input("Fornecedor 1: ")
valor_proposta1 = float(input("Valor proposta: "))

fornecedor2 = input("Fornecedor 2: ")
valor_proposta2 = float(input("Valor da 2° proposta: "))

if valor_proposta1 == valor_proposta2:
    print(f"{fornecedor1} e {fornecedor2} apresentaram propostas iguais. ")

elif valor_proposta1 > valor_proposta2:
    print(f"O fornecedor: {fornecedor2} apresentou o menor preço. ")

else:
    print(f"O fornecedor {fornecedor1} apresentou o menor preço. ")