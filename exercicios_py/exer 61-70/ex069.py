<<<<<<< HEAD
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
=======
mair18 = hms = mlhrmnr20 = 0
i = 1
while True:
    while True:
        sex =input(f'Digite o sexo da {i}º pessoa: ').strip().capitalize()

        if sex in ['Masculino', 'Feminino']:
            age = int(input(f'Digite a idade da {i}º pessoa: '))
>>>>>>> 7079f839a5fc008ca2798dd4135143ebf246838d
            break
        else:
            continue

<<<<<<< HEAD
    if esco in 'Não':
        break

print(f'Tem {quant_mair} pessoa(s) maior(es) de 18, {quant_h} homen(s) e {mlhr_mns20} mulher(es) menor(es) de 20 anos')
=======
    if age >= 18:
        mair18 += 1
    if sex in 'Masculino':
        hms += 1
    if age < 20 and sex in 'Feminino':  
        mlhrmnr20 += 1
    i += 1

    while True:
        esco = input('Quer continuar? (S/N): ').capitalize().strip()

        if esco in ['Sim', 'Não']:
            break
        else:
            print('opção inválida!')
            continue

    if esco in 'Não':
        break

print(f'{mair18} pessoas tem mais de 18 anos\n{hms} pessoas são homens\n{mlhrmnr20} são mulheres menores de 20 anos')
>>>>>>> 7079f839a5fc008ca2798dd4135143ebf246838d
