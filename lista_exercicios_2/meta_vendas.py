nome_vendedor = input("Digite o nome do vendedor: ")
valor_total_vendas = float(input(f"Digite o valor total de vendas de {nome_vendedor}: "))


if valor_total_vendas >= 15000:
    print(f"Você fez um trabalho excelente, {nome_vendedor}")

elif valor_total_vendas >= 10000:
    print(f"Meta atingida! Parabéns, {nome_vendedor} ")

else:
    print(f"Meta não atingida, {nome_vendedor}")