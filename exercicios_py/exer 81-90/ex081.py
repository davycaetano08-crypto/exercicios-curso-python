numeros = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    while True:
        esco = input('Quer continuar?: ').strip().upper()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('escolha inválida!')

    if esco == 'N':
        break
print(f'Você digitou {len(numeros)} números')

if 5 in numeros:
    print(f'O número 5 apareceu na posição {numeros.index(5)}')
else:
    print('O número 5 não foi digitado')

numeros.sort(reverse=True)
print(f'Lista em ordem decrescente: {numeros}')