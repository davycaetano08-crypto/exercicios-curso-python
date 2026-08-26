s = 0
c = 0
num = int(input('Digite um número: '))

for i in range(1, num + 1, 2):
    if i % 3 == 0:
        c += 1
        s += i

print(f'A soma dos {c} números ímpares e multiplos de 3 é {s}')
