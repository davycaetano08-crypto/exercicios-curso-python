from random import choice

valores = ['Pedra', 'Papel', 'Tesoura']
vez_pc = choice(valores)
print(vez_pc)
vez_jog = input('Escolha uma jogada:\n Pedra, Papel ou tesoura: ').capitalize()

if vez_pc == valores[0] and vez_jog == valores[1]:
    print(f'{vez_pc}!\nParabéns, você ganhou!')
elif vez_pc == valores[0] and vez_jog == valores[2]:
    print(f'{vez_jog}!\nEu ganhei! ha ha ha')
elif vez_pc == vez_jog:
    print(f'{vez_pc}!\nQue pena, empatamos!')
else:
    if vez_pc == valores[1] and vez_jog == valores[0]:
        print(f'{vez_pc}!\nEu ganhei! ha ha ha')
    elif vez_pc == valores[1] and vez_jog == valores[2]:
        print(f'{vez_pc}!\nParabéns, você ganhou!')
    elif vez_pc == vez_jog:
        print(f'{vez_pc}!\nQue pena, empatamos!')
    else:
        if vez_pc == valores[2] and vez_jog == valores[1]:
            print(f'{vez_pc}!\nEu ganhei! ha ha ha')
        elif vez_pc == valores[2] and vez_jog == valores[0]:
            print(f'{vez_pc}!\nParabéns, você ganhou!')
        else:
            print(f'{vez_pc}!\nQue pena, empatamos!')
            