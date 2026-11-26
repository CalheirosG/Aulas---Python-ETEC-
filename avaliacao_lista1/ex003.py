# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês 

ganhos_por_hora = float(input("Digite o valor em R$ que você recebe por hora: R$"))
horas_trabalhadas = int(input("Digite as horas totais trabalhadas no mês: "))

salario_total = ganhos_por_hora * horas_trabalhadas

print(f"O seu salário no referido mês será de R$ {salario_total:.2f} ")