maior = cont = menor = soma = 0

while True:
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = num
        menor = num
        cont += 1
        soma += num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        soma += num
        cont += 1
    esco = input('Quer contiuar? (S/N): ').upper()
    if esco == 'S':
        continue
    else:
        break

print(f'O maio número foi {maior}, o menor foi {menor} e a média {soma / cont}')