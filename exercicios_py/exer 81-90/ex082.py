num = []

while True:
    n = int(input('Digite um número: '))
    num.append(n)

    while True:
        esco = input('Quer continuar? (S/N): ').strip().upper()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('Input inválido')

    if esco == 'N':
        break
    
par = []
impar = []

for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Valores digitados: {num}\nValores pares: {par}\nValores ímpares: {impar}')