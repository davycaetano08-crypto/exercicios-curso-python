a = float(input('Digite o valor do 1° lado do triângulo:\n'))
b = float(input('Digite o valor do 2° lado do triângulo:\n'))
c = float(input('Digite o valor do 3° lado do triângulo:\n'))

if a < b + c and b < a + c and c < b + a:
    print(f'Os lados {a}, {b} e {c} podem formar um triângulo')
else:
    print(f'Os lados {a}, {b} e {c} \033[31;40mnão\033[m podem formar um triângulo')
