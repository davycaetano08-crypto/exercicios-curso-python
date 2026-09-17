numeros = []
while True:
    num = int(input('Digite um número: '))

    if num not in numeros:
        numeros.append(num)
    else:
        print('Número já digitado!')
        pass

    while True:
        esco = input('Quer continuar? S/N: ').strip().upper()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('Input inválido')

    if esco == 'N':
        break

print(f'Números únicos digitados: {sorted(numeros)}')