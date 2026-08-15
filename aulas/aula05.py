frase = 'Curso em Vídeo Python'

'''
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
'''

'''
print(frase)
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
'''
'''
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

'''

'''
frase = '   Aprenda Python  '

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
'''

#print(frase.split())
frase = frase.split()
print('-'.join(frase))