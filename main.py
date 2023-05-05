import pygame
from pygame.locals import *
from sys import exit


pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Crazy Snake")
relogio = pygame.time.Clock()

while True:
    relogio.tick(100)
    tela.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20

    if pygame.key.get_pressed()[K_a]:
        x = x - 5
    if pygame.key.get_pressed()[K_d]:
        x = x + 5
    if pygame.key.get_pressed()[K_w]:
        y = y - 5
    if pygame.key.get_pressed()[K_s]:
        y = y + 5
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    pygame.draw.rect(tela, (0, 0, 255), (200, 300, 40, 50))

    pygame.display.update()