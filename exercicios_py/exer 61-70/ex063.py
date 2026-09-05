atual = 1
anterior = 0
term = int(input('Quantos termos da sequência quer ver?: '))
cont = soma = 0

if term == 1:
    print(anterior, atual)
else:
    print(f'{anterior} {atual}', end=' ')
    while cont < term:
        soma = anterior + atual
        print(f'{soma}', end=' ')
        anterior = atual
        atual = soma
        cont += 1
