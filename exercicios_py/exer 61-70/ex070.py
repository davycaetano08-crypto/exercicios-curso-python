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
            continue

    if esco in 'Não':
        break
    

print(f'O total da compra é: {tot}R$\n{PrecoMs1000} produtos custam mais de 1000R$\nO produto mais barato é: {Prodbrt}')