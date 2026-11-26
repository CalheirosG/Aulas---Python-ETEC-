salario_cliente = float(input("Digite o seu salário: "))
valor_parcela = float(input("Digite o valor da parcela desejada: "))

diferenca_valor = salario_cliente * 30 / 100

if valor_parcela <= diferenca_valor:
    print("Empréstimo aprovado! ")

else:
    print("Empréstimo reprovado! ")

