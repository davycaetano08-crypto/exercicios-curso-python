preco_og = float(input('Qual o preço do seu produto?: '))
desc = float(input('Quanto desconto você quer aplicar? (%): '))

presc_desc = preco_og - (preco_og * (desc / 100))

print(f'O novo preço é de {presc_desc:.2f}R$, desconto aplicado: {preco_og * desc / 100}R$')