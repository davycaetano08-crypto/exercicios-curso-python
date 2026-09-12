classific = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Coritiba', 'Atlético-MG', 'Red Bull Bragantino', 'São Paulo', 'Vitória', 'Corinthians', 'Santos', 'Botafogo', 'Grêmio', 'Mirassol', 'Vasco', 'Internacional', 'Remo', 'Chapecoense')


while True:
    opc = int(input('[1]: top 5\n[2]: últimos 4\n[3]: Ordem alfabética\n[4]: posição time\n[0]: Sair\n'))
    if opc == 1:
        for i, time in enumerate(classific[:5]):
            print(f'{i + 1}°', time)
        continue
    elif opc == 2:
        for i, time in enumerate(classific[-1:-5:-1]):
            print(f'{20 - i}°', time)
        continue
    elif opc == 3:
        for i, time in enumerate(sorted(classific)):
            print(f'{i + 1}°', time)
        continue
    elif opc == 4:
        while True:
            esco_time = input('Qual time quer ver?: ').strip().capitalize()
            for i, time in enumerate(classific):
                if time == esco_time:
                    print(f'O {time} está na posição: {i + 1}°')
                    break
            if esco_time not in classific:
                print(f'O {esco_time} não está disputando a série A')
            break
    elif opc == 0:
        break
    else:
        print('Escolha inválida!')
        continue
