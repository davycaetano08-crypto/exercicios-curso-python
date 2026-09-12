numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',  'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Escolha um número (0 - 20): '))

    if num <= 20:
        break
    else:
        print('Valor inválido, tente novamente: ')

print(f'O número {num} por extenso é {numeros[num]}')