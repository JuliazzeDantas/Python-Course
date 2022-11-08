'''Exercise: Write a program to play a MP3'''

import pygame

musica = input("Digite o caminho da música que vc deseja ouvir: ")

pygame.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
