from datetime import date

maior_de_idade = 0
menor_de_idade = 0

for i in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {i}° pessoa nasceu?: '))
    if date.today().year - ano_nasc >= 21:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print(f'Quantidade maiores de idade: {maior_de_idade}\nQuantidade menores de idade: {menor_de_idade}')
        