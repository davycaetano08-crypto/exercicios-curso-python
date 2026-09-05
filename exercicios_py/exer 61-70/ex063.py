atual = 1
anterior = 0
term = int(input('Quantos termos da sequência quer ver?: '))
cont = soma = 0

if term == 1:
    print(f'{anterior}, {atual}')
else:
    print(anterior)
    print(atual)
    while cont < term:
        soma = anterior + atual
        anterior = atual
        atual = soma
        print(soma)
        cont += 1
