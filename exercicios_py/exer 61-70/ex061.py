num = int(input('Digite um número: '))
factorial = 1
num_reg = num

while num != 0:
    factorial = num * factorial
    num -= 1

print(f'O fatorial de {num_reg} é: {factorial}')