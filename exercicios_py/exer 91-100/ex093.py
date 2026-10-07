jogador = {}
gols = []
jogador['Nome'] = input('Nome do jogador: ').strip().title()
quantt_part = int(input('Quantidade de partidas: '))

for i in range(1, quantt_part + 1):
    gols.append(int(input(f'Quantidade de gols na {i}° partida: ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print()

for k, v in jogador.items():
    print(f'{k}: {v}')
print()

print(jogador)
print(f'O jogador {jogador["Nome"]} jogou {quantt_part} jogos\n')
for c, i in enumerate(gols):
    print(f'Na {c + 1}° partida, o jogador marcou {i} gols')
