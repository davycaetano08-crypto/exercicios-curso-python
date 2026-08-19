import time

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

notas = []
limite_notas = int(input('Quantas notas teve?: '))

for i in range(1, limite_notas + 1):
    i = float(input(f'Digite sua {i}º nota: '))
    notas.append(i)

m = sum(notas) / len(notas)

if m == 10:
    print(f'Sua média foi {m}! Parabéns')
elif m >= 8:
    print(f'Sua média foi {m}! Praticamente perfeito')
elif m >= 6:
    print(f'Sua média foi {m} Pode melhorar')
else:
    print(f'Sua média foi {m}.....')