a = float(input('Digite o valor do 1° lado do triângulo:\n'))
b = float(input('Digite o valor do 2° lado do triângulo:\n'))
c = float(input('Digite o valor do 3° lado do triângulo:\n'))

def is_triangle(a, b, c): # checa se realmente é um triângulo
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a < b + c and b < a + c and c < b + a

def get_triangle_type(a, b, c): #determina o tipo do triângulo
    if a == b == c:
        print('equilátero!')
    elif (a == c) or (b == c) or (a == b):
        print('isóceles!')
    else:
        print('escaleno!')


if is_triangle(a, b, c):
    print(f'Os lados {a}, {b}, {c} podem formar um triângulo {get_triangle_type(a, b, c)}')
else:
    print(f'Os lados {a}, {b}, {c} não podem formar um triângulo')
    