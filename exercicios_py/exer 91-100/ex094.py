pessoas, mlhrs, mais_avg_idd = [], [], []
dados = {}
sm_idd = 0

while True:
    dados['Nome'] = input('Nome: ').strip().title()
    dados['Sexo'] = input('Sexo: ').strip().capitalize()[0]
    dados['Idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())

    while True:
        esco = input('Quer continuar (S/N): ').strip().capitalize()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('Opção inválida!')

    if esco == 'N':
        break

print(f'\nQuantidade de pessoas: {len(pessoas)}')

for p in pessoas:
    sm_idd += p['Idade']
    if p['Sexo'] == 'F':
        mlhrs.append(p.copy())

avg_idd = sm_idd / len(pessoas)

for p in pessoas:
    if p['Idade'] > avg_idd:
        mais_avg_idd.append(p.copy())

print(f'Média de idade: {avg_idd:.1f}')
print(f'Mulheres cadastradas:', end=' ')

for p in mlhrs:
    print(p['Nome'], end=' ')

print(f'\nPessoas com idade acima da média: ')

for p in mais_avg_idd:
    for k, v in p.items():
        print(f'{k} = {v}', end=' ')
    print()
