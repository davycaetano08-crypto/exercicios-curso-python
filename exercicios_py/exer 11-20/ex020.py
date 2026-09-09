import random

alunos = []
limite_alunos = int(input('Quantos alunos tem?: '))

while len(alunos) in range(limite_alunos):
    nome = input('Escolha Qual o nome do aluno?: ')
    alunos.append(nome)

print(f'O aluno escolhido foi: {random.choice(alunos)}')
