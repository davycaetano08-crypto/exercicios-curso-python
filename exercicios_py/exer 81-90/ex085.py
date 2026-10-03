num = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}° valor: '))

    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()

print(f'Valores digitados: {num}\nNúmeros pares: {num[0]}\nNúmeros ímpares: {num[1]}')
