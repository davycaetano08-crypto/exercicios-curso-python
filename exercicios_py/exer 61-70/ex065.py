maior = cont = menor = soma = 0

while True:
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
        cont += 1
        soma += num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        soma += num
        cont += 1

    while True:
        esco = input('Quer contiuar? (S/N): ').upper().strip()
        if esco in ['Sim', 'Não']:
            break
        else:
            continue

    if esco in 'Sim':
        continue
    else:
        break            

print(f'O maior número foi {maior}, o menor foi {menor} e a média {soma / cont}')