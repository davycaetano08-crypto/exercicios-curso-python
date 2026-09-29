parent = []

expre = input('Digite uma expressão: ').strip().replace(' ', '')

for i in expre:
    if i == '(':
        parent.append(i)
    elif i == ')':
        parent.pop()

if len(parent) > 0:
    print(f'A operação {expre} é inválida!')
else:
    print(f'A operação {expre} é válida')
