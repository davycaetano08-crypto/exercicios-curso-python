import time
import random

'''
tempo = int(input('Quanto ano tem seu carro?: '))

if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')
'''
'''
nome = input('Digite seu nome: ').capitalize()
time.sleep(1.5)

if nome == 'Davy':
    print('Fala programador!')
else:
    print('Que nome paia....')
    time.sleep(2)
print(f'Olá {nome}.')
'''

'''
notas = []
limite_notas = int(input('Quantas notas teve?: '))

for i in range(1, limite_notas + 1):
    i = float(input(f'Digite sua {i}º nota: '))
    notas.append(i)

m = sum(notas) / len(notas)

if m == 10:
    print(f'Sua média foi \033[1;32m{m:.1f}\033[m! Parabéns')
elif m >= 8:
    print(f'Sua média foi \033[1;32m{m:.1f}\033[m! Praticamente perfeito')
elif m >= 6:
    print(f'Sua média foi \033[1;33m{m:.1f}\033[m Pode melhorar')
else:
    print(f'Sua média foi \033[1;31m{m:.1f}\033[m.....')

'''
'''
for i in range(0, 7, 2):
    print(i)
print('Fim')
'''
import math

print(int((2.2360679775)))