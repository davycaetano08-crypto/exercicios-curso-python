palavras = ('arroz', 'suco', 'alegria', 'pedra')

for palavra in palavras:
    letras = list(palavra)

    print(f'\nA palavra {palavra} tem as vogais: ', end='')
    for i in range(len(letras)):
        if letras[i] in ('a', 'e', 'i', 'o', 'u'):
            print(letras[i], end=' ')