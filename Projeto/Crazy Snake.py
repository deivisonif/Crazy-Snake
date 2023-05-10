import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

#Declaração de variáveis em geral: 

largura = 640
altura = 480
x_cobra = largura/2
y_cobra = altura/2
x_maca = randint(40, 600)
y_maca = randint(50, 430)
fonte = pygame.font.SysFont("Arial", 40, True, False)
pontos = 0
pygame.mixer.music.set_volume(0.2)
musicafundo = pygame.mixer.music.load("smw_castle_clear.wav")
pygame.mixer.music.play(-1)
barulhocoli = pygame.mixer.Sound("smw_jump.wav")
imagem_fundo = pygame.image.load('imagem_fundo.jpg')
comprimentoini = 5
velocidade = 10
xcontrole = 20
ycontrole = 0

#Fim da declaração de variáveis.

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Crazy Snake")
relogio = pygame.time.Clock()
lista_cobra = []
def aumentacobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 20, 20))
while True:
    relogio.tick(100)
    tela.fill((255,255,255))
    tela.blit(imagem_fundo, (0, 0))
    mensagem = f"Pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if xcontrole == velocidade:
                    pass
                else:
                    xcontrole = -velocidade
                    ycontrole = 0
            if event.key == K_RIGHT:
                if xcontrole == -velocidade:
                    pass
                else:
                    xcontrole = velocidade
                    ycontrole = 0
            if event.key == K_UP:
                if ycontrole == velocidade:
                    pass
                else:
                    ycontrole = -velocidade
                    xcontrole = 0
            if event.key == K_DOWN:
                if ycontrole == -velocidade:
                    pass
                else:
                    ycontrole = velocidade
                    xcontrole = 0
    x_cobra = x_cobra + (xcontrole/10)
    y_cobra = y_cobra + (ycontrole/10)
    x_cobra = x_cobra + (xcontrole/10)
    y_cobra = y_cobra + (ycontrole/10)

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulhocoli.play()
        comprimentoini = comprimentoini + 2
    

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    if len (lista_cobra) > comprimentoini:

        del lista_cobra[0]
           

    aumentacobra (lista_cobra)
    tela.blit(texto_formatado, (420, 40))
    pygame.display.update()
