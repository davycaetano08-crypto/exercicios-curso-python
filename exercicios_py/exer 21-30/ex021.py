import random
import time

alunos = []
limite_lista = int(input('Quantos alunos tem?: '))

while len(alunos) in range(limite_lista):
    nome = input('Qual o nome do aluno?: ')
    alunos.append(nome.capitalize())

print(f'A lista não embaralhada é: {alunos}')
random.shuffle(alunos)
time.sleep(2)

print(f'A ordem de apresentação é: {alunos}')
