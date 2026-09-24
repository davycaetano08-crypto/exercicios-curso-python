numeros = []

for i in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)

print(f'O maior número é: {max(numeros)}, nas posições:', end=' ')
for c, n in enumerate(numeros):
    if n == max(numeros):
        print(c, end=' ')

print(f'\n O menor número é: {min(numeros)}, nas posições:', end=' ')
for c, n in enumerate(numeros):
    if n == min(numeros):
        print(c, end=' ')