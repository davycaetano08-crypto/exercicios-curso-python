import math

cate_1 = float(input('Digite o comprimento de primeiro cateto: '))
cate_2 = float(input('Digite o comprimento do segundo cateto: '))
hipot = (cate_1 ** 2) + (cate_2 ** 2)

print(f'A a hipôtenusa dos catetos {cate_1} e {cate_2} é {math.sqrt(hipot)}')
