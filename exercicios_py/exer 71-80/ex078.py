num = []

for _ in range(4):
    num.append(int(input('Digite um valor: ')))


print(f'O maior número digitado foi: {max(num)}, nas posições: ', end=' ')
for c, i in enumerate(num):
    if i == max(num):
        print(c, end=' ')
print(f'\nO menor número digitado foi: {min(num)}, nas posições: ', end=' ')
for c, i in enumerate(num):
    if i == min(num):
        print(c, end=' ')
