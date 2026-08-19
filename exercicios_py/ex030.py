velo_car = int(input('Digite a velocidade do carro:\n'))
limite_via = int(input('Qual era o limite da vida?:\n'))

if velo_car > limite_via:
    print(f'Aplique uma multa de {(velo_car - limite_via) * 7}R$!')
else:
    print('Deixe seguir, o motorista estava dentro do limite')