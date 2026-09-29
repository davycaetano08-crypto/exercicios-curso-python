numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))

    while True:
        esco = input('Quer continuar?: ').strip().capitalize()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('Valor inválido!')

    if esco == 'N':
        break

par, impar = [], []

for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Valores digitados: {numeros}')
print(f'Valore pares digitados: {par}')
print(f'Valores ímpares digitados: {impar}')