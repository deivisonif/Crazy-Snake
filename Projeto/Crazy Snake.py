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
x_bloco_preto = randint(40, 600)
y_bloco_preto = randint(50, 430)
bloco_preto = pygame.Rect(x_bloco_preto, y_bloco_preto, 20, 20)  # Adicione essa linha
pygame.mixer.music.set_volume(0.2)
musicafundo = pygame.mixer.music.load("smw_castle_clear.wav")
pygame.mixer.music.play(-1)
barulhocoli = pygame.mixer.Sound("smw_jump.wav")
imagem_fundo = pygame.image.load('imagem_fundo.jpg')
comprimentoini = 5
velocidade = 10
xcontrole = 20
ycontrole = 0
fundo_imagem = pygame.image.load("Crazy Snake.png")
fundo_imagem2 = pygame.image.load("Crazy SnakeLost.png")


#Fim da declaração de variáveis.

tela = pygame.display.set_mode((largura, altura),)
pygame.display.set_caption("Crazy Snake")

#loop
running = True
while running:
    #verificar eventos de entrada
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            running = False # Encerrar a tela de início se qualquer tecla for pressionada

    # desenhar o fundo e a mensagem de inicio na tela
    tela.blit(fundo_imagem, (0,0))
    # atualizar tela
    pygame.display.flip()

relogio = pygame.time.Clock()
lista_cobra = []
def aumentacobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 20, 20))

def reiniciar_jogo():
    global pontos, x_cobra, y_cobra, lista_cobra, comprimento_inicial, x_maca, y_maca, x_controle, y_controle
    pontos = 0
    x_cobra = largura / 2
    y_cobra = altura / 2
    lista_cobra = []
    comprimento_inicial = 5
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    x_controle = 20
    y_controle = 0
    pygame.mixer.music.play(-1)

while True:
    tela.blit(imagem_fundo, (0, 0))
    bloco_preto = pygame.draw.rect(tela, (0, 0, 0), bloco_preto)
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

    if x_cobra < 0 or x_cobra > largura or y_cobra < 0 or y_cobra > altura:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reiniciar_jogo()
                    elif event.key == pygame.K_s:
                        pygame.quit()
                        exit()
            tela.blit(fundo_imagem2, (0, 0))
            pygame.display.flip()
                

                    

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    bloco = pygame.draw.rect(tela, (0, 0, 0), bloco_preto)

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulhocoli.play()
        comprimentoini = comprimentoini + 10

    if cobra.colliderect(bloco):
        x_bloco_preto = randint(40, 600)
        y_bloco_preto = randint(50, 430)
        bloco_preto = pygame.Rect(x_bloco_preto, y_bloco_preto, 20, 20)
        pygame.display.flip()
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reiniciar_jogo()
                    elif event.key == pygame.K_s:
                        pygame.quit()
                        exit()
            tela.blit(fundo_imagem2, (0, 0))
            pygame.display.flip()   
    

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            reiniciar_jogo()
                        elif event.key == pygame.K_s:
                            pygame.quit()
                            exit()
                tela.blit(fundo_imagem2, (0, 0))
                pygame.display.flip()



    if len (lista_cobra) > comprimentoini:

        del lista_cobra[0]
           
    aumentacobra (lista_cobra)
    tela.blit(texto_formatado, (420, 40))
    pygame.display.update()
