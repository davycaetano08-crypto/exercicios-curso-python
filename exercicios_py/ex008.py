lista_notas = []
limite_notas = int(input('Defina uma quantidade de notas: '))

for i in range(1, limite_notas + 1):
    i = float(input(f'Digite sua {i}º nota: '))
    lista_notas.append(i)

avg = sum(lista_notas) / len(lista_notas)

print(f'A média de todas as suas notas é: {avg:.2}')
