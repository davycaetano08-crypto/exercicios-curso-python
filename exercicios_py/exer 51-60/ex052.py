first_term = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = first_term + (10 - 1) * r

for i in range(first_term, dec + r, r):
    print(f'{i} ', end='-> ')
print('fim')
