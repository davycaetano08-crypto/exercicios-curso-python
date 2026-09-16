import time
from pygame import mixer

mixer.init()
while True:
    esco = int(input('Escolha a música:\n[1] Ato II - catarse\n[2] Papel de Parede\n'))
    
    if esco == 1:    
        mixer.music.load("assets/ato2_catarse.mp3")
    elif esco == 2:
        mixer.music.load("assets/papel_de_parede.mp3")

    print('Tocando.....')
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(1)

    while True:
        choice = input('Quer continuar? (S/N): ').strip().upper()

        if choice in ['S', 'N']:
            break
        else:
            print('Input inválido')
            continue

    if choice == 'N':
        break
    print('Música finalizada')
