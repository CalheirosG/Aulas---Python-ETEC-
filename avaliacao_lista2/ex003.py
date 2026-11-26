# Faça um programa que verifique se uma letra digitada corresponde a masculino ou feminino 

genero = input("""
Digite o seu gênero:
               
[m] - MASCULINO
[f] - FEMININO
""")

if genero == 'm':
    print("MASCULINO")

elif genero == 'f':
    print("FEMININO")

else:
    print("Gênero inválido, tente novamente! ")


