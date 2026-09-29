valores = []

while True:
    try:
        num = int(input('Digite um valor: '))

        if num not in valores:
            valores.append(num)
        else:
            print('Valor já digitado: ')

        while True:
            try:
                esco = input('Quer continuar? (S/N): ').strip().capitalize()[0]

                if esco in ['S', 'N']:
                    break
                else:
                    print('Valor inválido!')
            except IndexError:
                print('Digite algo!')

        if esco == 'N':
            break
    except ValueError:
        print('Digite algo!')

valores.sort()
print(f'Valores digitados: {valores}')
