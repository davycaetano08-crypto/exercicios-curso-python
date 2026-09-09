numeros = []

while True:
    num = int(input('Digite um número (999 para sair): '))

    if num == 999:
        break
    numeros.append(num)

print(f'O total de números é: {len(numeros)} e a soma: {sum(numeros)}')
