import random

def sorteio():
    from time import sleep
    numeros = []

    print(f'Os valores sorteados são: ')

    for i in range(5):
        numeros.append(random.randint(1, 50))
        print(f'{numeros[i]} ', end='')
        sleep(.5)

    return numeros

def somaPar(lst):
    soma = 0
    
    for i in lst:
        if i % 2 == 0:
            soma = soma + i
    return soma

valores = sorteio()

print(f'\nA soma dos valores pares em {valores} é {somaPar(valores)}')