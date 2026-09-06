prod_barat = ''
preco_barat = mais_d_1000 = soma = 0

while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))

    soma += preco

    if prod_barat == '':
        prod_barat = produto
        preco_barat = preco
    else:
        if preco < preco_barat:
            prod_barat = produto

    if preco >= 1000:
        mais_d_1000 += 1

    while True:
        esco = input('Quer continuar? (S/N): ').strip().upper()[0]

        if esco in ['S', 'N']:
            break
        else:
            continue

    if esco in 'Não':
        break

print(f'O total da sua compra foi {soma:.2f}, o produto mais barato foi ({prod_barat}) e um total de {mais_d_1000} produtos custam mais que R$1000,00')