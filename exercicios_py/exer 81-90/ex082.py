numeros = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    while True:
        esco = input('Quer continuar?: ').strip().upper()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('Escolha inválida')

    if esco == 'N':
        break

impar = [] 
par = []

for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Todos os números: {numeros}\nNúmeros pares: {par}\nÍmpares: {impar}')