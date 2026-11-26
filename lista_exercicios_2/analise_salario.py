nome_funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário atual do funcionário: "))
percentual = 0

if salario <= 2000:
    percentual = 10
    porcentagem_aumento = salario * 10 / 100

elif salario <= 5000:
    percentual = 7
    porcentagem_aumento = salario * 7 / 100

else:
    percentual = 5
    porcentagem_aumento = salario * 5 / 100

novo_salario = salario + porcentagem_aumento

print(f"""
Salário atual: R${salario:.2f}
Percentual de aumento: {percentual}%
Valor do aumento: R${porcentagem_aumento:.2f}
Novo salário: R${novo_salario:.2f}
""")

