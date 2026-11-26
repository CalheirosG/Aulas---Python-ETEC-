nome_vendedor = input("Digite o nome do vendedor: ")
valor_vendas = float(input(f"Digite o valor total vendido por {nome_vendedor}: "))

if valor_vendas >= 20000:
    percentual_comissao = "10%"
    comissao = valor_vendas * 0.10
    total_vendas = valor_vendas + comissao

elif valor_vendas >= 10000:
    percentual_comissao = "7%"
    comissao = valor_vendas * 0.7
    total_vendas = valor_vendas + comissao

else:
    percentual_comissao = "5%"
    comissao = valor_vendas * 0.5
    total_vendas = valor_vendas + comissao

print(f"O valor vendido por {nome_vendedor} foi de: R${valor_vendas:.2f}")
print(f"O percentual de comissão foi de: {percentual_comissao} ")
print(f"O valor da comissão foi de: R${comissao:.2f}")
