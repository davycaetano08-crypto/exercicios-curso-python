import math

while True:
    angulo = float(input('Digite um ângulo (0 - 360): '))
    
    if angulo >= 0 and angulo <= 360:
        print(f'O seno de {angulo}º é {math.sin(angulo):.2f} e o cosseno é {math.cos(angulo):.2f}')
        break
    else:
        print('Ângulo inválido!')
        pass