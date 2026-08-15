frase = 'Curso em Vídeo Python'

'''
print(frase[3])
print(frase[1:15])
print(frase[1:15:2])
print(frase[:13])
print(frase[13:])
print(frase[::2])
'''

'''
print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an expericed programmer in any programming language
(whatever it may be) can pick Python very quickly.
It's also easy for beginners to use and learn, so jump in""")
'''

print(frase)
print(len(frase.strip()))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

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