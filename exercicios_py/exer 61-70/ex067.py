while True:
    n = int(input('Número inteiro (digite um número negativo para sair): '))

    if n >= 0:
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')
    else:
        print('Programa encerrado')
        break