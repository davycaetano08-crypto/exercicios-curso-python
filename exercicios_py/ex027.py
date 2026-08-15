frase = input('Digite uma frase: ')

print(f'A letra "A" aparece {frase.lower().find('a')}')
print(f'e aparece primeiro na posição: {frase.lower().replace(' ', '').index('a')}')
print(f'e por ultimo na posição: {frase.lower().replace(' ', '').rindex('a')}')
