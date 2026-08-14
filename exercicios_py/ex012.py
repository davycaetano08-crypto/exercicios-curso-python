larg = float(input('Digite a largura da parede: '))
compr = float(input('Digite o comprimento da parede: '))
#Quanto um balde cobre
cobert_balde = 2

print(f'Para a sua parede, precisa de {(larg * compr) / cobert_balde:.2f} baldes')
