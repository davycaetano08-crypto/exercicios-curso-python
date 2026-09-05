from random import randint

num = randint(1, 5) #computador escolhe um número aleatório

print(('-=-' * 15),'\nVou escolher um número aleatório')
print('-=-' * 15)

while True:
    escol_user = int(input('Escolha um número entre 1 e 5:\n'))
    if escol_user == num:
        print('Parabéns, você acertou o número!')
        break
    else:
        print(f'Que pena...\ntente novamente')
