import time
from pygame import mixer

mixer.init()

# escolher a musica
mixer.music.load("ato2_catarse.mp3")
#mixer.music.load("papel_de_parede.mp3")

print('Tocando.....')
mixer.music.play()

while mixer.music.get_busy():
    time.sleep(1)

print('Música finalizada')
