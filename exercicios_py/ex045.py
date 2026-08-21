valor_produto = float(input('Qual o valor do produto?: '))

while True:
    modo_pagg = int(input('Escolha o modo de pagamento:\n[1] dinheiro/cheque\n[2] cartão a vista\n[3] cartão parcelado\n'))
    if modo_pagg == 1:
        print(f'O valor da sua compra é {valor_produto - (valor_produto * .10)}')
        break
    elif modo_pagg == 2:
        print(f'O valor da sua compra é {valor_produto - (valor_produto * .05)}')
        break
    elif modo_pagg == 3: #caso pagamento seja em cartão parcelado
        quant_parcela = int(input('Escolha a quantidade de parcelas: '))

        if quant_parcela <= 2:
            print(f'O valor da sua compra é {valor_produto}')
        else:
            print(f'O valor da sua compra é {valor_produto + (valor_produto * .2)}')
            break
    else:
        print('Método inválido!, tente novamente')
