expr = input('Digite a expressão: ').strip().replace(' ', '')
pilha = []

for i in expr:
    if i == '(':
        pilha.append(i)
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(i)
            break

if len(pilha) == 0:
    print(f'A expressão: {expr} é válida!')
else:
    print(f'A expressão: {expr} é inválida!')    