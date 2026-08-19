slr = float(input('Digite seu salário atual:\n'))

if slr >= 1250:
    print(f'Seu novo salário é {slr + (slr * 0.1)}')
else:
    print(f'Seu novo salário é {slr + (slr * 0.15)}')