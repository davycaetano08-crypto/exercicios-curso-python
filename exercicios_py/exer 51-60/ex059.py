from random import randint

num = randint(0, 10)
quant = 0

while True:
    escol = int(input('Escolha um número: '))

    if escol == num:
        print('Parabéns! Você acertou')
        quant += 1
        break
    elif escol < num:
        print('Tá quase, o número é maior!')
        quant += 1
    else:
        print('Tá quase, o número é menor!')
        quant += 1
print(f'Você acertou o número: {num} em {quant} tentativas')