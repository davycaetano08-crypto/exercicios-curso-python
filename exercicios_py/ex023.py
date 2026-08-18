import time

nome = input('Qual o seu nome completo?: ')
nome_sep = nome.split()

print('Analisando seu nome.....')
time.sleep(2)

print(nome.upper())
print(nome.lower())
print(f'O seu nome tem um total de {len(nome.replace(' ', ''))} letras')
print(f'O seu primeiro nome tem {len(nome_sep[0])} letras')

