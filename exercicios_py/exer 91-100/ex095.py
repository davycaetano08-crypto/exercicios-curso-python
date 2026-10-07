jogador = {}
jogadores, gols = [], []

while True:
    jogador['Nome'] = input('Nome do jogador: ').strip().title()
    quantt_part = int(input('Quantidade de partidas: '))
    for i in range(1, quantt_part + 1):
        gols.append(int(input(f'Quantidade de gols na partida {i}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = len(gols)
    jogadores.append(jogador.copy())
    gols.clear()

    while True:
        jog = input('Quer continuar?: ').strip().capitalize()[0]

        if jog in ['S', 'N']:
            break
        else:
            print('Opção inválida!')
    if jog == 'N':
        break

    
for j in jogadores:
    for k, v in j.items():
        print(f'{k}: {v}')
    print()

while True:
    jog = input('Que jogador quer ver?: ').strip().title()

    for p in jogadores:
        if jog == p['Nome']:
            print(f'O jogador {p["Nome"]} jogou {p["total"]} jogos\n')
            for c, i in enumerate(p['gols']):
                print(f'Na partida {c + 1}, o jogador marcou {i} gols')

    while True:
        esco = input('Quer continuar?: ').strip().capitalize()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('Input inválido!')

    if esco == 'N':
        break