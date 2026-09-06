from random import randint

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