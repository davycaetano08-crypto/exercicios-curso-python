peso_kg = float(input('Digite seu peso em KG: '))
altura_m = float(input('Digite sua altura em METROS: '))
imc = peso_kg / altura_m ** 2
def get_imc(imc: float):
    if imc < 18.5:
        classificacao ='abaixo do peso'
    elif imc <= 25:
        classificacao ='peso ideal'
    elif imc <= 30:
        classificacao ='sobrepeso'
    elif imc <= 40:
        classificacao ='obesidade'
    else:
        classificacao ='obesidade mórbida'
    return classificacao

if peso_kg == 0 or altura_m == 0:
    print('Peso ou altura inválido!')
else:
    print(f'Seu IMC é {imc:.2f} e se enquadra como: {get_imc(imc)}')