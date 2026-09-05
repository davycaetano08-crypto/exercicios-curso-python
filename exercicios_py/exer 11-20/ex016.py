dias_alug = int(input('Por quantos dias foi alugado?: '))
km_roda = float(input('Quantos quilômetros foram rodados?: '))

total_pago = (dias_alug * 60) + (km_roda * 0.15)
print(f'O total a ser pago é: {total_pago:.2f}R$')
