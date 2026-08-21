num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num1} é menor que {num2}')
else:
    print(f'{num1} é igual a {num2}')