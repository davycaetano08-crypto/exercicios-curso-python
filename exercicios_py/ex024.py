while True:
    num = input('Digite um número 0 - 9999: ')
    if int(num) <= 9999:
        print(f'''        unidade:{num[3]}
        dezena:{num[2]}
        centena:{num[1]}
        milhar:{num[0]}''')
        break
    else:
        print('número inválido!')
