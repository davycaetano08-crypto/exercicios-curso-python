pessoas, dados = [], []
maior_pes = menor_pes = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    while True:
        esco = input('Quer continuar?: ').strip().capitalize()[0]
        if esco in ['S', 'N']:
            break
        else:
            print('Input inválido!')
    if esco == 'N':
        break

for c, i in enumerate(pessoas):
    if c == 0:
        maior_pes = i[1]
        menor_pes = i[1]
    else:
        if i[1] > maior_pes:
            maior_pes = i[1]
        elif i[1] < menor_pes:
            menor_pes = i[1]

print(f'Quantidade de pessoas: {len(pessoas)}')
print(f'Pessoas mais pesadas ({maior_pes}Kg):', end=' ')
for p in pessoas:
    if p[1] == maior_pes:
        print(f'[{p[0]}]', end=' ')

print(f'\nPessoas mais leves ({menor_pes}Kg):', end=' ')
for p in pessoas:
    if p[1] == menor_pes:
        print(f'[{p[0]}]', end=' ')