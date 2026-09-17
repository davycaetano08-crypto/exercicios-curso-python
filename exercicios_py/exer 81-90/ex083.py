expr = (input('digite uma expressão: ')).strip().replace(' ', '')
elementos = list(expr)

print(elementos)

for i in elementos:
    if i == '(':
        print('parentesis')