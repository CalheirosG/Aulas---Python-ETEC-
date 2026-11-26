peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * 2)

if imc <= 18.5:
    print("Abaixo do peso ")

elif imc <= 24.9:
    print("Peso normal ")

elif imc <= 34.9:
    print("Obesidade Grau | ")

elif imc <= 39.9:
    print("Obesidade Grau || ")

elif imc >= 40:
    print("Obesidade Grau ||| ")

else:
    print("Não atende nenhum critério, tente novamente! ")

print(imc)