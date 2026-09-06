som = cont = 0
while True:
    try:
        num = int(input('Digite um número: '))
        if num != 999:
            som += num
            cont += 1
        else:
            break
    except ValueError:
        print('Input inválido!, digite um número inteiro!')
        continue
print(f'A soma dos {cont} valores é {som}')