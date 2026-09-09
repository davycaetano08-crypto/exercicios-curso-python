s = 0

for i in range(1, 7):
    n = int(input(f'Digite o {i}° número: '))
    if n % 2 == 0:
        s += n

print(f'A soma dos números é: {s}')