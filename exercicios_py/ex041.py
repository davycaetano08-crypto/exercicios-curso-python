notas = []
limite_notas = int(input('Quantas notas teve?: '))

for i in range(1, limite_notas + 1):
    i = float(input(f'Digite sua {i}º nota: '))
    notas.append(i)

m = sum(notas) / len(notas)

if 7 > m >= 5:
    print(f'Com uma média de {m:.1f}, você ficou de recuperação!')
elif m >= 7:
    print(f'Com uma média de {m:.1f}, Você passou direto!')
else:
    print(f'Com uma média de {m:.1f}, Você está reprovado!')