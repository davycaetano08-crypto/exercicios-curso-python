import math

cate_1 = float(input('Digite o comprimento do cateto oposto: '))
cate_2 = float(input('Digite o comprimento do cateto adjacente: '))
hipot = math.hypot(cate_1, cate_2)

print(f'A a hipôtenusa dos catetos {cate_1} e {cate_2} é {hipot:.2f}')
