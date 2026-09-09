for i in range(1, 6):
    peso = float(input(f'{i}° pessoa\nDigite seu peso: '))
    if i == 1:
        peso_max = peso
        peso_min = peso
    if peso > peso_max:
        peso_max = peso
    if peso < peso_min:
        peso_min = peso

print(f'O maior peso é: {peso_max}, e o menor é: {peso_min}')