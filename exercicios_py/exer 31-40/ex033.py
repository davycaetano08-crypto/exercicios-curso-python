import calendar

ano = int(input('Escolha um ano:\n'))

if calendar.isleap(ano) == True:
    print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto!')
    