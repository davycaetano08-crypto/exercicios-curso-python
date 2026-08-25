a = 'anotaram a data da maratona'
a = a.replace(' ', '')

if a == a[::-1]:
    print(f'{a} é um palíndromo.')
else:
    print(f'{a}não é um palíndromo')