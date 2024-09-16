import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    vitorias_usuario = 0
    vitorias_maquina = 0
    empates = 0

    while True:

        escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()

        if escolha_usuario == 'sair':
            break
        elif escolha_usuario not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue


        escolha_maquina = random.choice(opcoes)
        print(f"Máquina escolheu: {escolha_maquina}")


        if escolha_usuario == escolha_maquina:
            print("Empate!")
            empates += 1
        elif (escolha_usuario == 'pedra' and escolha_maquina == 'tesoura') or \
                (escolha_usuario == 'tesoura' and escolha_maquina == 'papel') or \
                (escolha_usuario == 'papel' and escolha_maquina == 'pedra'):
            print("Você venceu!")
            vitorias_usuario += 1
        else:
            print("Máquina venceu!")
            vitorias_maquina += 1


    print(f"\nResultados finais:")
    print(f"Vitórias do usuário: {vitorias_usuario}")
    print(f"Vitórias da máquina: {vitorias_maquina}")
    print(f"Empates: {empates}")

jogar()
