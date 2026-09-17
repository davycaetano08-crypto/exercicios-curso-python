num = []

for i in range(5):
    num.append(int(input(f'Digite o {i}° valor: ')))

print(f'Você digitou {num}')

print(f'O maior número é {max(num)} na posição {num.index(max(num))}')
print(f'O menor número é {min(num)}, na posição {num.index(min(num))}')