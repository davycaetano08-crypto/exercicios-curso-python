def maior(num):
    nmr_maior = 0
    
    for i in num:
        if i > nmr_maior:
            nmr_maior = i

    print(f'O maior número entre {num} é {nmr_maior}')


numeros = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    while True:
        resp = input('Quer continuar?: ').strip().capitalize()[0]

        if resp in ['S', 'N']:
            break
        else:
            print('Input inválido!')

    if resp == 'N':
        break

maior(numeros)