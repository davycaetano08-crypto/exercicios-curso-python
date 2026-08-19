import math

an = float(input('Digite um ângulo (0 - 360): '))

print(f'O seno de {an}º é {math.sin(math.radians(an)):.2f},o cosseno é {math.cos(math.radians(an)):.2f} e a tangente é: {math.tan(math.radians(an)):.2f}')
