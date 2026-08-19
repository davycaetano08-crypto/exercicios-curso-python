nome = input('Digite seu nome: ').capitalize()
cores = {'limpa':'\033[m', 
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'
}

print(f'É um prazer te conhecer, {cores['azul']}{nome}{cores['limpa']}!')
