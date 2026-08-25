from datetime import date

maior_de_idade = 0
menor_de_idade = 0

for i in range(0, 7):
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    if date.today().year - ano_nasc < 21:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print(f'Quantidade maiores de idade: {maior_de_idade}\nQuantidade menores de idade: {menor_de_idade}')
        