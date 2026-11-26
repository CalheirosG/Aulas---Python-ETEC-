produtos = [
    "bananas", "bolachas", "salgadinhos", "canetas", "borrachas", "lápis"
]

qtde_produtos = [16, 32, 30, 2, 88, 11]

# Nesse aqui eu me empolguei, hehe

for i, qtde in enumerate(qtde_produtos):
    if qtde < 10:
        print(f"{produtos[i]}: Estoque crítico, temos apenas {qtde} unidades. ")
    
    elif 10 < qtde < 30:
        print(f"{produtos[i]}: Estoque baixo, temos apenas {qtde} unidades. ")
    
    else:
        print(f"{produtos[i]}: Estoque adequado. ")





