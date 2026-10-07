pessoas, idd_acm_avg = [], []
dados = {}
sm_idd = 0

while True:
    dados['Nome'] = input('Nome: ').strip().title()

    while True:
        sexo = input('Sexo: ').strip().capitalize()[0]
        if sexo in ['M', 'F']:
            dados['Sexo'] = sexo
            break
        else:
            print('Digite apenas M ou F!')  

    dados['Idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    dados.clear()

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

avg_idd = sm_idd / len(pessoas)

for p in pessoas:
    if p['Idade'] > avg_idd:
        idd_acm_avg.append(p.copy())

print(f'Média de idade: {avg_idd:5.1f}')
print(f'Mulheres cadastradas:', end=' ')

for p in pessoas:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=' ')

print(f'\nPessoas com idade acima da média: ')

for p in idd_acm_avg:
    for k, v in p.items():
        print(f'{k} = {v}', end=' ')
    print()
