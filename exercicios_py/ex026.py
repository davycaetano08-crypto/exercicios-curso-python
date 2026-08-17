nome = input('Digite seu nome completo: ')
se_tem_nome =(nome.find('Silva'))

if se_tem_nome != -1:
    print(f'Seu nome ({nome}) tem Silva')
else:
    print(f'Seu nome ({nome}) não tem Silva')