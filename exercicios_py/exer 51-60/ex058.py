while True:
    sexo = input("Digite seu sexo (M/F): ").upper()

    if sexo in 'MF':
        print('Input Aceito!')
        break
    else:
        print('Input Inválido')