import pygame

pygame.init()
TELA_LARGURA = 400
TELA_ALTURA = 600
title = pygame.display.set_caption("PUM GAME!")
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))


branco=(255,255,255)
vermelho_escuro = (122, 27, 12)
cinza = (105,105,105)
cinza_escuro = (63,63,63)
verde_escuro = (63,93,63)
amarelo_esquesito = (120, 119, 27)

clock = pygame.time.Clock()
pygame.mixer.music.load('peido.wav')


