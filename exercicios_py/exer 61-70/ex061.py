num = int(input('Digite um número: '))
factorial = 1
c = num

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    factorial *= c
    c -= 1

print(factorial)