lista = []

while True:
    num = int(input('Digite um número, digite 999 para sair: '))
    if num != 999:
        lista.append(num)
    else:
        break
print(f'A soma dos {len(lista)} números digitados foi: {sum(lista)}')