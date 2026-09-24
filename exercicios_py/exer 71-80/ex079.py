vlrs = []

while True:
    num = int(input('Digite um número: '))
    if num not in vlrs:
        vlrs.append(num)
    else:
        print('número já digitado!')
        continue

    while True:
        esco = input('Quer continuar? (S/N): ').strip().upper()[0]

        if esco in ['S', 'N']:
            break
        else:
            print('Escolha inválida')

    if esco == 'N':
        break

print('Valores digitados:', end=' ')
for i in sorted(vlrs):
    print(i, end=' ')
