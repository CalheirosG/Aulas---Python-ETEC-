#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
# usuário informe um valor válido.

parar = False

while parar == False:
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if nota > 0 and nota <= 10:
        parar = True
    
    print("Opção inválida, digite uma nota entre 0 e 10! ")