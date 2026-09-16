numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',  'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Escolha um número (0 - 20): '))

    if 0 <= num <= 20:
        print(f'O número {num} por extenso é {numeros[num]}')

        while True:
            esco = input('Quer Continuar? S/N: ').strip().capitalize()[0]

            if esco in ['S', 'N']:
                break
            else:
                print('input Inválido!')
        if esco == 'N':
            break
    else:
        print('Valor inválido, tente novamente: ')

