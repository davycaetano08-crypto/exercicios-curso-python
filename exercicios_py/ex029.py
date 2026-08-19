import random

num = random.randint(1, 5)

while True:
    escol_user = int(input('Escolha um número entre 1 e 5:\n'))
    if escol_user == num:
        print('Parabéns, você acertou o número!')
        break
    else:
        print(f'Que pena...\ntente novamente')