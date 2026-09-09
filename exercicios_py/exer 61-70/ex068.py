from random import randint

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
