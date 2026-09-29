valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)

    while True:
        esco = input('Quer continuar? (S/N): ').strip().capitalize()

        if esco in ['S', 'N']:
            break
        else:
            print('Input inválido!')

    if esco == 'N':
        break

valores_inver = valores[:]
valores_inver.sort(reverse=True)

print(f'Quantidade de alores digitados: {len(valores)}')
print(f'Valores em ordem decrescente: {valores_inver}')

if 5 in valores:
    print('O número 5 está na lista, nas posições: ', end=' ')
    for c, i in enumerate(valores):
        if i == 5:
            print(c, end=' ')
else:
    print('O número 5 não está na lista')