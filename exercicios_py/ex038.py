num = int(input('Digite um número:\n'))
opc = int(input('Escolha uma base:\n[1]: binário\n[2]: octal\n[3]: hexadecimal\n'))

if opc == 1:
    print(f'O número {num} em binário é {bin(num)}')
elif opc == 2:
    print(f'O número {num} em base octal é {num % 8}')
elif opc == 3:
    print(f'O número {num} em base hexadecimal é {hex(num)}')
else:
    print('Operação inválida!')