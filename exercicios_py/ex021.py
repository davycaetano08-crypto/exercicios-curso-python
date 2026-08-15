import random

alunos = ['lucas', 'Gabriel', 'Helena', 'Rafael',
           'Bianca', 'Leonardo']
limite_lista = 6
ordem = random.sample(alunos, limite_lista)

print(f'A ordem de apresentação é: {ordem}')