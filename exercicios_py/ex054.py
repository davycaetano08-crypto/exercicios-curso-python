palavra = input('Digite uma frase: ').strip().replace(' ', '').lower()

if palavra == palavra[::-1]:
    print(f'{palavra} é um palíndromo.')
else:
    print(f'{palavra} não é um palíndromo')
