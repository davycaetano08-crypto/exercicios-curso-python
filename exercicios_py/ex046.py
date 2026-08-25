from random import choice

valores = ('Pedra', 'Papel', 'Tesoura')
computador = choice(valores)
jogador = input('Escolha uma jogada:\n Pedra, Papel ou Tesoura: ').capitalize()

if computador == valores[0] and jogador == valores[1]:
    print(f'{computador}!\nParabéns, você ganhou!')
elif computador == valores[0] and jogador == valores[2]:
    print(f'{jogador}!\nEu ganhei! ha ha ha')
elif computador == jogador:
    print(f'{computador}!\nQue pena, empatamos!')
else:
    if computador == valores[1] and jogador == valores[0]:
        print(f'{computador}!\nEu ganhei! ha ha ha')
    elif computador == valores[1] and jogador == valores[2]:
        print(f'{computador}!\nParabéns, você ganhou!')
    elif computador == jogador:
        print(f'{computador}!\nQue pena, empatamos!')
    else:
        if computador == valores[2] and jogador == valores[1]:
            print(f'{computador}!\nEu ganhei! ha ha ha')
        elif computador == valores[2] and jogador == valores[0]:
            print(f'{computador}!\nParabéns, você ganhou!')
        else:
            print(f'{computador}!\nQue pena, empatamos!')
            