ltr_cmc = input('Escolha um nome/letra para começar: ')
cidade = input('Digite sua cidade: ')


if cidade.title().startswith(ltr_cmc.title()):
    print(f'Sua cidade {cidade.title()} começa com {ltr_cmc.title()}')
else:
    print(f'A cidade {cidade.title()} não começa com {ltr_cmc.title()}')