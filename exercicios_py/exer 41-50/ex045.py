print(f'{' Lojona Top ':=^40}')

valor_produto = float(input('Qual o valor do produto?: '))

while True:
    modo_pagamento = int(input('Escolha o modo de pagamento:\n[1] dinheiro/cheque\n[2] cartão a vista\n[3] cartão parcelado\n'))

    if modo_pagamento == 1:
        print(f'O valor da sua compra é {valor_produto - (valor_produto * .1):.2f}R$')
        break
    elif modo_pagamento == 2:
        print(f'O valor da sua compra é {valor_produto - (valor_produto * .05):.2f}R$')
        break
    elif modo_pagamento == 3: #caso pagamento seja em cartão parcelado
        quant_parcela = int(input('Escolha a quantidade de parcelas: '))

        if quant_parcela <= 2:
            print(f'O valor da sua compra é {valor_produto:.2f}R$')
            break
        else:
            valor_produto = valor_produto + (valor_produto * .2)
            print(f'O valor da sua compra parcelada em {quant_parcela} vezes de {valor_produto / quant_parcela:.2f}, é {valor_produto :.2f}R$')
            break
    else:
        print('Método inválido!, tente novamente')
