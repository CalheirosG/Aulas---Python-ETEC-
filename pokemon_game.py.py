import time
import random




print("=" * 10, "JOGO - POKEMON", "=" * 10)

pokemons = ["Bulbasaur", "Pikachu", "Squirtle", "Ivysaur", "Charmander", "Charmeleon", "Blastoise", "Butterfree"]



while True:

    ataque_maquina = random.randint(5, 15)
    vida_maquina = random.randint(60, 100)
    

    ataque_jogador = random.randint(5, 15)
    vida_jogador = random.randint(60, 100)

    pokemon_maquina = random.choice(pokemons)

    nome_jogador = input("Qual o seu nome, viajante? ")
    print(f"{nome_jogador}, né? Me parece familiar... ")
    time.sleep(3)
    

    print(f"{nome_jogador}, temos uma batalha a frente! Nosso oponente é um {pokemon_maquina}, o que você prefere fazer?")
    try:
        opcoes_partida = int(input("[1] - Batalhar\n[2] - Ignorar\n"))
        
        if opcoes_partida == 1:
            print("Certo, vamos batalhar!")
            time.sleep(2)
            for i, pokemon in enumerate(pokemons):
                print(f"{i+1} - {pokemon}")
            
            opcao_pokemon = int(input("Selecione o seu Pokemon:"))
            pokemon_jogador = f"{pokemons[opcao_pokemon-1]}"
            print("\n\n\n")

            print(f"""O pokemon escolhido foi {pokemon_jogador}!
Ataque: {ataque_jogador}
Vida: {vida_jogador}\n""")
            time.sleep(2)

            print(f"{pokemon_jogador} | HP: {vida_jogador} | ATQ: {ataque_jogador}")
            print("=" * 12, "VS", "=" * 12)
            print(f"{pokemon_maquina} | HP: {vida_maquina} | ATQ: {ataque_maquina}")
            print("\n\n\n")
        
        elif opcoes_partida == 2:
            print("Nem todas as batalhas são nossas... Vamos embora")
            time.sleep(3)
            print("...")
            
            break

        else:
            print("Opção inválida, tente novamente! ")
            continue
        

    except ValueError:
        print("Opção inválida, tente novamente.")
        
        
        
    while True:

        ataque_maquina = random.randint(5, 15)
        cura_maquina = random.randint(1, 15)

        ataque_jogador = random.randint(5, 15)
        cura_jogador = random.randint(1, 15)

        try:
            opcao_batalha = int(input("[1] - ATACAR\n[2] - CURAR\n[3] - FUGIR\n"))
        
        except ValueError:
            print("Opção inválida, selecione uma das opções informadas.")
            opcao_batalha = int(input("[1] - ATACAR\n[2] - CURAR\n[3] - FUGIR\n"))
        
        if opcao_batalha == 1:
            print(f"Você lançou um ataque e causou {ataque_jogador} de dano.")
            time.sleep(2)
            print(f"Seu oponente atacou, você recebeu {ataque_maquina} de dano.")
            time.sleep(2)
            print("=" * 15)

            vida_jogador -= ataque_maquina
            vida_maquina -= ataque_jogador

            if vida_jogador < 0:
                vida_jogador = 0
            
            elif vida_maquina < 0:
                vida_maquina = 0

            print(f"Você possui {vida_jogador} pontos de vida. ", end="| ")
            print(f"O seu oponente possui {vida_maquina} pontos de vida. ")

            if vida_jogador <= 0 or vida_maquina <= 0:
                if vida_maquina <= 0:
                    print("Você venceu, é melhor irmos andando... ")
                    break
            
                else:
                    print("Infelizmente você foi derrotado. ")
                    break
        
        elif opcao_batalha == 2:
            print(f"Você usou um feitiço de cura que te concedeu {cura_jogador} pontos de vida.")
            time.sleep(2)
            vida_jogador += cura_jogador

            cura_maquina_opcao = random.randint(1, 2)

            if cura_maquina_opcao == 1:
                print(f"Seu oponente utilizou um feitiço de cura que concedeu {cura_maquina} pontos de vida.")
                time.sleep(2)
                vida_maquina += cura_maquina

                print(f"Você possui {vida_jogador} pontos de vida. ", end="| ")
                time.sleep(2)
                print(f"O seu oponte possui {vida_maquina} pontos de vida. ")
            
            else:
                print(f"Seu oponente atacou, você recebeu {ataque_maquina} de dano")
                time.sleep(2)
                vida_jogador -= ataque_maquina
        
        elif opcao_batalha == 3:
            print(f"Eu acho que realmente um {pokemon_maquina} era demais para nós... as vezes a melhor estratégia é recuar... ")
            time.sleep(5)
            break

        else:
            print("Opção inválida, tente novamente! ")
            continue

    
    try:
        continuar = int(input("Deseja jogar novamente?\n[1] - SIM\n[2] - NÃO\n"))
    
    except ValueError:
        continuar = 2
    
    if continuar != 1:
        print(f"Até a próxima, {nome_jogador}! ")
        break
    

        



