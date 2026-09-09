dist = float(input('Qual a distância percorrida em KM?:\n'))

if dist <= 200:
    print(f'O preço da sua passagem é R${dist * 0.5:.2f}')
else:
    print(f'O preço da sua passagem é R${dist * 0.45:.2f}')

print('Boa viagem!')
