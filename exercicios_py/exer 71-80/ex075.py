n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

numeros = (n1, n2, n3, n4)

print(f'Total de vezes que 9 aparece: {numeros.count(9)}')

if 3 not in numeros:
    print('O 3 não foir digitado')
else:
    print(f'Index do número 1º número 3: {numeros.index(3)}')

for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')