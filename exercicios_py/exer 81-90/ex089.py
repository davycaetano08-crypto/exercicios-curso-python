alunos, aluno, notas = [], [], []

while True:
    aluno.append(input('Adicione o nome do aluno: ').strip().capitalize())
    while len(notas) < 2:
        notas.append(float(input('Digite as notas do aluno: ')))
    aluno.append(notas[:])
    notas.clear()

    alunos.append(aluno[:])
    aluno.clear()

    while True:
        esco = input('Tem mais algum aluno?: ').strip().capitalize()[0]
        if esco in ['S', 'N']:
            break
        else:
            print('Escolha inválida!')

    if esco == 'N':
        break

for a in alunos:
    print(f'Aluno: {a[0]}')
    print(f'Média {sum(a[1]) / len(a[1])}')


while True:
    choice = input('Digite um nome: ').strip().capitalize()

    for a in alunos:
        if a[0] == choice:
            print(f'Notas do aluno {a[0]}: {a[1]}')
    while True:
        mais = input('Quer ver mais algum aluno?: ').strip().capitalize()

        if mais in ['S', 'N']:
            break
        else:
            print('Input inválido!')
    if mais == 'N':
        break