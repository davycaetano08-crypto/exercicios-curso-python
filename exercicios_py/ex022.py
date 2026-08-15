import time
from pygame import mixer

mixer.init()

mixer.music.load("minha_musica.mp3")

print('Tocando.....')
mixer.music.play()

while mixer.music.get_busy():
    time.sleep(1)

print('Música finalizada')