primeTerm = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
limite = int(input('Quantos termos quer ver?: '))
cont = 1

while limite != 0:
    if limite != 0:
        if cont < limite + 1:
            if cont == 1:
                TermAtu = primeTerm
                cont += 1
                print(f'{primeTerm}', end=' ')
            else:
                print(f'{TermAtu + razao}' , end=' ')
                TermAtu += razao
                cont += 1
        else:
            esco = int(input('Quantos termos a mais que ver?: '))
            if esco != 0:
                limite += esco
            else:
                break