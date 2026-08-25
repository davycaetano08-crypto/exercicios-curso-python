from time import sleep

first_term = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for i in range(1, 11):
    if r < 0:
        n = first_term + (r * i)
    elif r > 0:
        n = first_term + r * i
    print(f'O número na {i}° posição é {n}')
    sleep(0.5)