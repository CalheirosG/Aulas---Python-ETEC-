# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# Que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total. 

metros_quadrados_area = float(input("Digite a área a ser pintada M²: "))

litros_latas = 18

preco_lata = 80

total_latas = metros_quadrados_area // 18

preco_total = total_latas * preco_lata

print(f"A área que será pintada é de {metros_quadrados_area}m².")
print(f"Serão necessárias {total_latas:.0f} lata para realizar a pintura. ")
print(f"O preço total das latas será de R${preco_total:.2f} ")




