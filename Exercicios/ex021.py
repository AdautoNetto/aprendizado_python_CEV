import pygame  # importa a biblioteca pygame
import time    # para pausar o programa (opcional)

# inicializa o mixer do pygame
pygame.mixer.init()

# carrega o arquivo de música (tem que estar na mesma pasta do código)
pygame.mixer.music.load('mscex021.mp3')

# inicia a reprodução da música
pygame.mixer.music.play()

# espera a música terminar (por exemplo, 10 segundos)
time.sleep(10)
