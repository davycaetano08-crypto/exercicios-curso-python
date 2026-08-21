from math import pow

peso = float(input('Digite seu peso em KG: '))
altt = float(input('Digite sua altura em METROS: '))
imc = peso / pow(altt, 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} (abaixo do peso)')
elif imc <= 25:
    print(f'Seu IMC é {imc:.2f} (peso ideal)')
elif imc <= 30:
    print(f'Seu IMC é {imc:.2f} (sobrepeso)')
elif imc <= 40:
    print(f'Seu IMC é {imc:.2f} (obesidade)')
elif imc > 40:
    print(f'Seu IMC é {imc:.2f} (obesidade mórbida)')