<<<<<<< HEAD
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
=======
tot = mnrPreco = PrecoMs1000 = 0
Prodbrt = ''

while True:
    nomeProd = input('Nome: ').strip().lower()
    preco = float(input('Preço: '))

    if Prodbrt == '':
        mnrPreco = preco
        Prodbrt = nomeProd

    if preco < mnrPreco:
        Prodbrt = nomeProd
    if preco > 1000:
        PrecoMs1000 += 1

    tot += preco

    while True:
        esco = input('Quer continuar? (S/N): ').capitalize().strip()

        if esco in ['Sim', 'Não', 'S', 'N']:
            break
        else:
            print('opção inválida!')
>>>>>>> 7079f839a5fc008ca2798dd4135143ebf246838d
            continue

    if esco in 'Não':
        break
<<<<<<< HEAD

print(f'O total da sua compra foi {soma:.2f}, o produto mais barato foi ({prod_barat}) e um total de {mais_d_1000} produtos custam mais que R$1000,00')
=======
    

print(f'O total da compra é: {tot}R$\n{PrecoMs1000} produtos custam mais de 1000R$\nO produto mais barato é: {Prodbrt}')
>>>>>>> 7079f839a5fc008ca2798dd4135143ebf246838d
