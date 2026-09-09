while True:
    sexo = input("Digite seu sexo (M/F): ").capitalize().strip()[0]

    if sexo in ('MF'):
        print(f'Input ({sexo}) Aceito!')
        break
    else:
        print('Input Inválido')