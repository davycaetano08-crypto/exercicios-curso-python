slr_og = float(input('Digite seu salário: '))
aumento = float(input('Qual o aumento?: '))

print(f'Seu novo salário é {slr_og + (slr_og * (aumento / 100)):.2f}R$')
