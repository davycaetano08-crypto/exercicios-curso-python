a = float(input('Digite o valor do 1° lado do triângulo:\n'))
b = float(input('Digite o valor do 2° lado do triângulo:\n'))
c = float(input('Digite o valor do 3° lado do triângulo:\n'))

def is_triangulo(a, b, c): # checa se realmente é um triângulo
    if a < b + c and b < a + c and c < b + a:
        print(f'Os lados {a}, {b} e {c} podem formar um triângulo')
        return True
    else:
        print(f'Os lados {a}, {b} e {c} \033[31;40mnão\033[m podem formar um triângulo')
        return False

def get_tipo_triangulo(a, b, c): #determina o tipo do triângulo
    if a == c and b == c:
        print('Este é um triângulo equilátero!')
    elif (a == c) or (b == c) or (a == b):
        print('este é um triângulo isóceles')
    else:
        print('Este é um triângulo escaleno')


if is_triangulo(a, b, c) == True:
    get_tipo_triangulo(a, b, c)
