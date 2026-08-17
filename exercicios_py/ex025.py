comec_com = input('Escolha um nome/letra para começar: ')
cidade = input('Digite sua cidade: ')


if cidade.title().startswith(comec_com.title()):
    print(f'Sua cidade {cidade.title()} começa com {comec_com.title()}')
else:
    print(f'A cidade {cidade.title()} não começa com {comec_com.title()}')