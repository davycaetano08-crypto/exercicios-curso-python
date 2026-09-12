from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)

numeros = (n1, n2, n3, n4, n5)

for i in numeros:
    print(i, end=' ')

print(f'\nMaior número: {max(numeros)}\nMenor número: {min(numeros)}')