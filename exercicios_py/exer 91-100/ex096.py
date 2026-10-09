def area(larg, comp):
    print(f'A área do retângulo: {larg}x{comp} é: {comp * larg}m²')


l = float(input('Digite a largura do retângulo: '))
c = float(input('Digite a comprimento do retângulo: ').replace(',', '.'))

area(l, c)