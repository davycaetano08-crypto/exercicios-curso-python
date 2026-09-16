from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for i in numeros:
    print(i, end=' ')

print(f'\nMaior número: {max(numeros)}\nMenor número: {min(numeros)}')