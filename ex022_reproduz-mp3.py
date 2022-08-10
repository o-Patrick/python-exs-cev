# 22. Faça um programa que abra e reproduza um arquivo MP3.
# Não toca :sad:

import pygame
pygame.init()
pygame.mixer.music.load('ex022-into-the-dark.mp3')
# pygame.mixer.music.load('exs/ex022-into-the-dark.mp3')
pygame.mixer.music.play()
pygame.event.wait()
