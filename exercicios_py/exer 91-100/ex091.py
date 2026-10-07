from random import randint
from time import sleep
from operator import itemgetter

jogador = {}

for i in range(1, 5):
    jogador[f'Jogador{i}'] = randint(1, 6)
    sleep(0.5)
    print(f'O Jogador {i} tirou: {jogador[f'Jogador{i}']}')

ranking = []
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'O {i + 1}° lugar é {v[0]}, que tirou {v[1]}')