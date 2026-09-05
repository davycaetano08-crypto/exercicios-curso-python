num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}')

print(f'Unidade {u:2}\nDezena {d:3}\nCentena {c:2}\nMilhar {m:3}')
