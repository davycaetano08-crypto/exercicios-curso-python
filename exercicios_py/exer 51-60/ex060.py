from time import sleep

while True:
    n1 = int(input('Digite o primero número: '))
    n2 = int(input('Digite o segundo número: '))

    esco = int(input('Escolha a operação:\n[1]: Soma\n[2]: Multiplicação\n[3]: Definir maior\n[4]: Novos números\n[5]: Sair do programa\n'))


    if esco == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        break
    elif esco == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
        break
    elif esco == 3:
        if n1 < n2:
            print(f'{n2} é o maior')
            break
        elif n1 > n2:
            print(f'{n1} é o maior')
            break
        else:
            print(f'Os dois número são iguais')
            break
    elif esco == 4:
        continue
    elif esco == 5:
        print(f'Até logo....')
        sleep(.3)
        break
    else:
        print('Input inválido!')
