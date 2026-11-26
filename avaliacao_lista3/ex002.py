# Faça um programa que leia um nome de usuário e senha e continue solicitando até que eles sejam distintos. 

nome_usuario = input("Digite o seu usuário: ")
senha = input("Senha: ")

while nome_usuario == senha:
    print("Erro! O nome de usuário e a senha não podem ser iguais! Tente novamente. ")

    nome_usuario = input("Digite o seu usuário: ")
    senha = input("Senha: ")