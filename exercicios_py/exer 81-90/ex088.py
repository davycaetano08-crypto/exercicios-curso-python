from random import randint
from time import sleep

nmr_jogos = int(input('Quantos jogos quer sortear: '))
jogos, numeros = [], []

for i in range(1, nmr_jogos + 1):
    while len(numeros) < 6:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    jogos.append(numeros[:])
    numeros.clear()

for c, i in enumerate(jogos):
    print(f'{c + 1}° jogo: {i}')
    sleep(.5)