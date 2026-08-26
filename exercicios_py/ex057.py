cadastro = []

for i in range(3):
    nome = input('Digite seu nome: ').capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: ').capitalize()

    dados_pessoa = {
        "name": nome,
        "age": idade,
        'sex': sexo
    }

    cadastro.append(dados_pessoa)
    print('Pessoa Cadastrada!')

for c in cadastro:
    print({c['name']}, {c['age']}, {c['sex']})