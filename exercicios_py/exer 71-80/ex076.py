produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 42.90)

for i in range(len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]:>6.2f}')
    