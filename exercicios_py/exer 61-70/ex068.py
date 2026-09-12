from random import randint

<<<<<<< HEAD
opc = ['par', 'ímpar']
vit = 0

while True:
    jogador = input('Escolha entre par ou ímpar: ')

    if jogador == opc[1]:
        computador = opc[0]
    else:
        computador = opc[1]

    jogada_pc = randint(1, 10)
    jogada_joga = int(input('Escolha sua jogada (1 - 10):'))

    if (jogada_pc + jogada_joga) % 2 == 0 and computador == opc[0]:
        print('O Computador venceu!')
        break
    elif (jogada_pc + jogada_joga) % 2 != 0 and computador == opc[0]:
        print('Você ganhou!')
        vit += 1
    elif (jogada_pc + jogada_joga) % 2 != 0 and computador == opc[1]:
        print('O computador venceu!')
        break
    else:
        print('Você ganhou!')
        vit += 1

print(f'Você perdeu depois de {vit} vitórias')
=======
vit = 0

while True:
    jogadas = ['par', 'ímpar']
    jogador = input('Escolha sua jogada (par, ímpar): ').strip().lower()

    while True:
        if jogador == jogadas[0]:
            computador = jogadas[1]
            break
        elif jogador == jogadas[1]:
            computador = jogadas[0]
            break
        else:
            jogador = input('Escolha sua jogada (par, ímpar): ').strip().lower()
    print(computador)

    jog_computador = randint(1, 10)
    jog_jogador = int(input('Escolha um número de 1 - 10: '))

    if jogador == jogadas[0]:
        if (jog_jogador + jog_computador) % 2 == 0:
            print('jogador venceu!')
            vit += 1
        else:
            print('Jogador perdeu!')
            break
    else:
        if (jog_jogador + jog_computador) % 2 != 0:
            print('jogador venceu!')
            vit += 1
        else:
            print('jogador perdeu!')
            break

print(f'Jogador perdeu depois de {vit} rodadas')
>>>>>>> 7079f839a5fc008ca2798dd4135143ebf246838d
