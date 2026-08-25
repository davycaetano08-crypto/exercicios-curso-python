from time import sleep

print(f'{' Estouro de fogos ':=^30}')
sleep(0.5)

for i in range(10, 0, -1):
    print(f'Os estouros acontecem em {i}')
    sleep(1)
print('Estouros!!!!!')