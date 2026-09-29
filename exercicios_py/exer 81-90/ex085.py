num, par, impar = [], [], []

for i in range(1, 8):
    n = int(input(f'Digite o {i}° valor: '))

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()

num.append(par[:])
num.append(impar[:])

print(f'Valores digitados: {num}\nNúmeros pares: {num[0]}\nNúmeros ímpares: {num[1]}')
