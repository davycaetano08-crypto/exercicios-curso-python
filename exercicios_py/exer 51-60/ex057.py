femi_menor_20 = 0
idades = 0
max_idade = 0

for i in range(1, 5):
    print(f'{f'{i}° Pessoa':-^20}')

    nome = input('Nome: ').capitalize().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper().strip()

    idades += idade

    if idade > max_idade and sexo == "M":
        max_idade = idade
        nome_h = nome

    if idade < 20 and sexo == 'F':
        femi_menor_20 += 1

print(f'O homem mais velho é o {nome_h}, com {max_idade} anos')
print(f'A média de idade é {(idades / 4):.1f}')
print(f'A quantidade de mulheres com menos de 20 anos é {femi_menor_20}')
