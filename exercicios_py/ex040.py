from datetime import date

ano_nasc = int(input('digite o ano em que nasceu: '))
diff_idade = date.today().year - ano_nasc

if diff_idade < 18:
    print(f'Você com {diff_idade} anos, ainda terá que se alistar, daqui a {18 - diff_idade} ano(s)')
elif diff_idade == 18:
    print(f'Você já tem {diff_idade} anos, ta na hora de se alistar!')
else:
    print(f'Se você ainda não se alistou, perdeu o prazo por {diff_idade - 18} anos')