print('==== Simulador de Empréstimo ====\n')

salario = float(input('Qual é o seu salário?: '))
valor_casa = float(input('Qual o valor da casa?: '))
quantt_parc = int(input('Em quantas vezes quer parcelar?: '))
preco_parc = valor_casa / quantt_parc

if preco_parc > (salario * 0.3):
    print(f'Empréstimo negado, o valor de parcela: R${preco_parc:.2f} excede 30% do seu salário')
else:
    print(f'Empréstimo aprovado, o valor da sua parcela é R${preco_parc:.2f}')