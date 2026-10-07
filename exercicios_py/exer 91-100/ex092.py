from datetime import date

dados = {}

dados['Nome'] = input('Nome: ').strip().title()

ano_nasc = int(input('Ano nasc: '))
dados['Idade'] = date.today().year - ano_nasc
num_cart_trb = int(input('Num Carteira de Trabalho (0 se não tiver): '))

if num_cart_trb != 0:
    dados['Numero Carteira'] = num_cart_trb
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Digite seu salário: ').replace(',', '.'))
    print()
    dados['Idade Para Aposentar'] = dados['Idade'] + (35 - (2026 - dados['Ano de Contratação']))

for k, v in dados.items():
    print(f'{k}: {v}')