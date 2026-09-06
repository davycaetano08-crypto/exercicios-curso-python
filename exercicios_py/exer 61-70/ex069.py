quant_h = quant_mair = mlhr_mns20 = 0
cont = 1

while True:
    idade = int(input(f'Digite a idade da {cont}° pessoa: '))
    sexo = input(f'Digite o sexo da {cont}° pessoa: ').strip().capitalize()[0]
    cont += 1

    if idade >= 18:
        quant_mair += 1
    if sexo == 'M':
        quant_h += 1
    if idade < 20 and sexo == 'F':
        mlhr_mns20 += 1

    while True:
        esco = input('Quer continuar? (S/N): ').upper().strip()[0]

        if esco in ['S', 'N']:
            break
        else:
            continue

    if esco in 'Não':
        break

print(f'Tem {quant_mair} pessoa(s) maior(es) de 18, {quant_h} homen(s) e {mlhr_mns20} mulher(es) menor(es) de 20 anos')