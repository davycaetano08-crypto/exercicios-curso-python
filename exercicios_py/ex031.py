from time import sleep

num = int(input('Digite um número: '))

for i in range(1, num + 1):
    sleep(.05)
    if i % 2 == 0:
        print(f'{i} é par!')
    else:
        print(f'{i} é ímpar')