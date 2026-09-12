<<<<<<< HEAD
som = cont = 0
while True:
    try:
        num = int(input('Digite um número: '))
        if num != 999:
            som += num
            cont += 1
        else:
            break
    except ValueError:
        print('Input inválido!, digite um número inteiro!')
        continue
print(f'A soma dos {cont} valores é {som}')
=======
numeros = []

while True:
    num = int(input('Digite um número (999 para sair): '))

    if num == 999:
        break
    numeros.append(num)

print(f'O total de números é: {len(numeros)} e a soma: {sum(numeros)}')
>>>>>>> 7079f839a5fc008ca2798dd4135143ebf246838d
