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
pygame.mixer.music.set_volume(1)
musicafundo = pygame.mixer.music.load("smw_castle_clear.wav")
pygame.mixer.music.play(-1)
barulhocoli = pygame.mixer.Sound("smw_jump.wav")
imagem_fundo = pygame.image.load('imagens/imagem_fundo.jpg')

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
    texto_formatado = fonte.render(mensagem, True, (255, 215, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = x - 20
            if event.key == K_RIGHT:
                x = x + 20
            if event.key == K_UP:
                y = y - 20
            if event.key == K_DOWN:
                y = y + 20

    if pygame.key.get_pressed()[K_LEFT]:
        x_cobra = x_cobra - 5
    if pygame.key.get_pressed()[K_RIGHT]:
        x_cobra = x_cobra + 5
    if pygame.key.get_pressed()[K_UP]:
        y_cobra = y_cobra - 5
    if pygame.key.get_pressed()[K_DOWN]:
        y_cobra = y_cobra + 5
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulhocoli.play()
    

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    aumentacobra (lista_cobra)
    tela.blit(texto_formatado, (420, 40))
    pygame.display.update()
