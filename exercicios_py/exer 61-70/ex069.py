mair18 = hms = mlhrmnr20 = 0
i = 1
while True:
    while True:
        sex =input(f'Digite o sexo da {i}º pessoa: ').strip().capitalize()

        if sex in ['Masculino', 'Feminino']:
            age = int(input(f'Digite a idade da {i}º pessoa: '))
            break
        else:
            continue

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