pesos = []

for i in range(1, 7):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    pesos.append(peso)

print(f'O maior peso é: {max(pesos)}KG, e o menor é {min(pesos)}KG')