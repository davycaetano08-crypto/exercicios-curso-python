'''
nome = input('Qual é o seu nome?: ')

print(f'Prazer em te conhecer {nome}!')
'''

n1 = int(input('Digite um Valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, a divisão é {d:.3f}, a multiplicação é {m}',
      f'a divisão inteira é {di} e a exponenciação é {e}')