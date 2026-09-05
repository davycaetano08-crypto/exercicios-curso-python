from random import randint

num = randint(1, 5) #computador escolhe um número aleatório

print(('-=-' * 15),'\nVou escolher um número aleatório')
print('-=-' * 15)

for i in range(1, 6):
    EscolPlay = int(input('Escolha um número: '))

    if EscolPlay == num:
        print('Parabéns, Você acertou')
        break
    elif EscolPlay < num:
        print('Foi quase, o número é maior!')
    else:
        print('Foi quase, o número é menor')
else:
    print(f'Sua tentativas acabaram! o número era {num}')