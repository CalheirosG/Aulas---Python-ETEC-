# Faça um programa que leia e valide as seguintes informações: {NOME, IDADE, SALÁRIO, ESTADO CIVIL}

nome = input("Digite o seu nome: ")

while len(nome) <= 3:
    print("O nome inserido precisa ter no mínimo 4 caracteres. ")
    nome = input("Digite o seu nome: ")

idade = int(input("Digite a sua idade: "))

while idade <= 0 or idade >= 150:
    print("Idade inválida, tente novamente. ")
    idade = int(input("Digite a sua idade: "))

salario = float(input("Digite o seu salário: "))

while salario <= 0:
    print("O salário não pode ser negativo, tente novamente. ")
    salario = input("Digite o seu salário: ")

estado_civil = input("""Digite o seu estado civil
                     [S] - SOLTEIRO
                     [C] - CASADO
                     [V] - VIÚVO
                     [D] - DIVORCIADO

                        """)

while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Opção inválida, selecione uma das opções citadas.")
    estado_civil = input("""Digite o seu estado civil
                     [S] - SOLTEIRO
                     [C] - CASADO
                     [V] - VIÚVO
                     [D] - DIVORCIADO

                        """)



    