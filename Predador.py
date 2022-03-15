import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.load('X2Download.com - 1 Hour of Relaxing Zelda_ Breath of the Wild Music (64 kbps).mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

som_de_pontuação = pygame.mixer.Sound('smw_coin.wav')
som_de_pontuação.set_volume(1)

fonte = pygame.font.SysFont('arial', 30, True, True)
pontos = 0

largura = 960
altura = 750
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('PREDADOR')
relogio = pygame.time.Clock()

yJogador = altura*3/4
xJogador = largura*3/4
areaDoJogador = 50
morreu = False

posiçãoy_retangulo_verde = randint(5, altura - 10)
posiçãox_retangulo_verde = randint(5, largura - 10)

raioDoInimigo = 30
xDoInimigo = largura/4
yDoInimigo = altura*3/4
velocidade_doInimigox = velocidade_doInimigoy = velocidadeDoJogador = velocidade_doInimigo2x = velocidade_doInimigo2y = 12.5
xDoInimigo2 = -100
yDoInimigo2 = -100

def reiniciar_jogo():
    global morreu, pontos, posiçãox_retangulo_verde, posiçãoy_retangulo_verde, areaDoJogador, yJogador, xJogador
    morreu = False
    pontos = 0
    posiçãoy_retangulo_verde = randint(5, altura - 10)
    posiçãox_retangulo_verde = randint(5, largura - 10)
    areaDoJogador = 50
    yJogador = -100
    xJogador = -100


while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    pontuação = f'POINTS: {pontos}'
    pontuação_formatada = fonte.render(pontuação, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_UP]:
        yJogador -= velocidadeDoJogador
    elif pygame.key.get_pressed()[K_DOWN]:
        yJogador += velocidadeDoJogador
    if pygame.key.get_pressed()[K_LEFT]:
        xJogador -= velocidadeDoJogador
    elif pygame.key.get_pressed()[K_RIGHT]:
        xJogador += velocidadeDoJogador

    retangulo_azul = pygame.draw.rect(tela, (0, 0, 255), (xJogador, yJogador, areaDoJogador, areaDoJogador))
    retangulo_verde = pygame.draw.rect(tela, (0, 255, 0), (posiçãox_retangulo_verde, posiçãoy_retangulo_verde, 10, 10))
    inimigo = pygame.draw.circle(tela, (255, 0, 0), (xDoInimigo, yDoInimigo), raioDoInimigo)
    inimigo2 = pygame.draw.circle(tela, (255, 0, 0), (xDoInimigo2, yDoInimigo2), raioDoInimigo)

    if pontos == 25:
        xDoInimigo2 = largura*3/4
        yDoInimigo2 = altura/4

    yDoInimigo -= velocidade_doInimigoy
    xDoInimigo += velocidade_doInimigox
    yDoInimigo2 -= velocidade_doInimigo2y
    xDoInimigo2 += velocidade_doInimigo2x

    if retangulo_azul.colliderect(retangulo_verde):
        posiçãoy_retangulo_verde = randint(10, altura - 10)
        posiçãox_retangulo_verde = randint(5, largura - 10)
        areaDoJogador += 2
        som_de_pontuação.play()
        pontos += 1

    if inimigo.colliderect(retangulo_azul) or inimigo2.colliderect(retangulo_azul):
        areaDoJogador -= 2

    if xJogador + 1 < 0:
        xJogador = 1
    elif xJogador + areaDoJogador / 2 > largura:
        xJogador = largura - areaDoJogador - 1
    if yJogador + 1 < 0:
        yJogador = 1
    elif yJogador + areaDoJogador / 2 > altura:
        yJogador = altura - areaDoJogador - 1

    if areaDoJogador == 0:
        morreu = True
        fonte2 = pygame.font.SysFont('arial', 50, True, True)

        while morreu:
            tela.fill((255, 255, 255))
            game_over = fonte2.render('GAME OVER', True, (255, 0, 0))
            recomeçar = fonte.render('Press r to start again', True, (255, 0, 0))
            rating = fonte.render(f'RATING: {pontos}', True, (0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            tela.blit(rating, (15, 15))
            tela.blit(recomeçar, (largura//2 - 145, altura//2 + 50))
            tela.blit(game_over, (largura//2 - 150, altura//2 - 10))
            pygame.display.flip()

    if xDoInimigo + raioDoInimigo > largura or xDoInimigo - raioDoInimigo < 0:
        velocidade_doInimigox = -velocidade_doInimigox
    if yDoInimigo + raioDoInimigo > altura or yDoInimigo - raioDoInimigo < 0:
        velocidade_doInimigoy = -velocidade_doInimigoy

    if xDoInimigo2 + raioDoInimigo > largura or xDoInimigo2 - raioDoInimigo < 0:
        velocidade_doInimigo2x = -velocidade_doInimigo2x
    if yDoInimigo2 + raioDoInimigo > altura or yDoInimigo2 - raioDoInimigo < 0:
        velocidade_doInimigo2y = -velocidade_doInimigo2y

    tela.blit(pontuação_formatada, (50, 50))
    pygame.display.flip()