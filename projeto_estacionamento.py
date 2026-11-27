vagas_estacionamento = []
faturamento = 0.0
TARIFA_ESTACIONAMENTO = 8
CAPACIDADE_TOTAL_ESTACIONAMENTO = 20



def verificar_vagas(lista):
    if len(lista) < 20:
        return True
    return False

def calcular_horas_estacionado(horas, tarifa):
    return horas * tarifa

def formatar(text):
    text = text.strip()
    text = text.replace("-", "")
    text = text.replace(".", "")
    text = text.replace("_", "")
    return text

while True: 
    print("=" * 10, "SISTEMA DE ESTACIONAMENTO", "=" * 10)


    print("""
[1] - Registrar entrada de veículo
[2] - Registrar saída de veículo
[3] - Consultar vagas disponíveis
[4] - Consultar faturamento
[0] - Encerrar programa
          """)
    
    try:
        opcao = int(input("Escolha uma opção:"))
        while True:
            if opcao == 1:
                if verificar_vagas(vagas_estacionamento):
                    placa_veiculo = str(input("Digite a placa do veículo:"))
                    placa_veiculo = formatar(placa_veiculo)

                    if len(placa_veiculo) == 7 and placa_veiculo.isalnum():

                        print("Veículo registrado com sucesso!")
                        vagas_estacionamento.append(placa_veiculo)
                        break

                else:
                    print("Estacionamento lotado!")
                    break
                
                print("Placa inválida, tente novamente.", end=" ")
        
        if opcao == 2:
            placa_veiculo_saida = input("Digite a placa do veículo que está saindo:")
            if placa_veiculo_saida in vagas_estacionamento:
                horas_estacionado = int(input("Digite a quantidade de horas estacionado: "))
                total_a_pagar = calcular_horas_estacionado(horas_estacionado, TARIFA_ESTACIONAMENTO)
                print(f"O valor total a ser pago pela permanência de {horas_estacionado} horas no estacionamento é de {total_a_pagar:.2f}R$")
                vagas_estacionamento.remove(placa_veiculo_saida)
                faturamento += total_a_pagar
            else:
                print("A placa informada não foi encontrada no sistema, tente novamente.")
                continue
        
        if opcao == 3:
            print(f"""
            A capacidade total do estacionamento é de {CAPACIDADE_TOTAL_ESTACIONAMENTO} vagas;
            Atualmente temos {len(vagas_estacionamento)} veículos estacionados;
            temos {CAPACIDADE_TOTAL_ESTACIONAMENTO - len(vagas_estacionamento)} vagas disponíveis""")
        
        if opcao == 4:
            print(f"O valor total arrecadado é de: R${faturamento:.2f}")
        
        if opcao == 5:
            print("=" * 10, "Obrigado por utilizar o Vehicle Control", "=" * 10)
            break






    except ValueError:
        print("Opção inválida, tente novamente.")
        continue

