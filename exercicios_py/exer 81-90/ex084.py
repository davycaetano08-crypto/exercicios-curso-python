pessoas, dado = [], []
maior_pes, menor_pes = 0, 0

while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()

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
        if i[1] >= maior_pes:
            maior_pes = i[1]
        elif i[1] <= menor_pes:
            menor_pes = i[1]

pessoas_mais_pes, pessoas_mais_lev = [], []

for i in pessoas:
    if i[1] == maior_pes:
        pessoas_mais_pes.append(i[0])
    elif i[1] == menor_pes:
        pessoas_mais_lev.append(i[0])


print(f'Quantidade de pessoas: {len(pessoas)}')
print(f'Pessoas mais pesadas ({maior_pes}KG): {pessoas_mais_pes}')
print(f'Pessoas mais leves ({menor_pes}KG): {pessoas_mais_lev}')