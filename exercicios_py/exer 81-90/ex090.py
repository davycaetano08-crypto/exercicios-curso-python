aluno = {}

aluno['Nome'] = input('Nome: ').strip().title()
aluno['media'] = float(input(f'Média do {aluno['Nome']}: ').replace(',', '.'))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('\nAnálise de notas\n')

for k, v in aluno.items():
    print(f'{k}: {v}')