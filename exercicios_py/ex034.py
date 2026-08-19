nums = []
limite_lista = int(input('Escolha o tamanho da lista:\n'))

for i in range(1, limite_lista + 1):
    i = float(input(f'Digite o {i}º número:\n'))
    nums.append(i)

print(f'O maior número é {max(nums)} e o menor é {min(nums)}')