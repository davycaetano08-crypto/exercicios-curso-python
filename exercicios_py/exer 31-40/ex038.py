from time import sleep

num = int(input('Digite um número:\n'))

while True:    
    opc = int(input('Escolha uma base:\n[1]: binário\n[2]: octal\n[3]: hexadecimal\n'))
    if opc == 1:
        print(f'O número {num} em binário é {bin(num)[2:]}')
        break
    elif opc == 2:
        print(f'O número {num} em base octal é {oct(num)[2:]}')
        break
    elif opc == 3:
        print(f'O número {num} em base hexadecimal é {hex(num)[2:]}')
        break
    else:
        print('Operação inválida!, Tente novamente')
        sleep(1.5)