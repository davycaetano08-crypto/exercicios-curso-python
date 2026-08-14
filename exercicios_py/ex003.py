num_01= int(input('Primeiro número: '))
num_02= int(input('Segundo número: '))

#checa se o número é negativo

if num_02 < 0:
    num_02 = num_02 * -1
else:
    pass

soma = num_02 + num_01

print(f'A soma de {num_01} e {num_02} é: {soma}')
