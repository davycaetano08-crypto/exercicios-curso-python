nome = input('Digite seu nome completo: ')
teste =(nome.find('Silva'))

if teste != -1:
    print(f'Seu nome ({nome}) tem Silva')
else:
    print(f'Seu nome ({nome}) não tem Silva')