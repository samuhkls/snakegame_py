import pygame
import time
import random

cobra_vel = 30

tela_x = 720
tela_y = 480

# cores

preto = pygame.Color(0, 0, 0)
branco = pygame.Color(255, 255, 255)
vermelho = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
azul = pygame.Color(0, 0, 255)

pygame.init()

# inicializando tela de gameplay
pygame.display.set_caption('cobrinhaaaa')
janela = pygame.display.set_mode((tela_x, tela_y))

fps = pygame.time.Clock()


cobra_pos = [300,50]

# primeiros blocos do corpo

cobra_corpo = [
    [300,50],
    [290, 50],
    [280, 50],
    [270, 50]
]

# spawn da fruta 
fruta_pos = [random.randrange(1, (tela_x//10)) * 10,
             random.randrange(1, (tela_y//10)) * 10]

fruta_spawn = True

# direção default da cobra
direcao = 'direita'
andar = direcao

# pontuacao inicial
pontos = 0

# MOSTRANDO PONTUAÇÃO
def mostra_pontuacao(escolha, cor, font, tamanho):

    ponto_font = pygame.font.SysFont(font, tamanho)

    ponto_superficie = ponto_font.render('Pontos : ' + str(pontos), True, cor)

    ponto_rect = ponto_superficie.get_rect()

    janela.blit(ponto_superficie, ponto_rect)


def gameover():
    # criando um objeto pra fonte
    fonte = pygame.font.SysFont('comicsansms', 50)
    # criando uma superficie pra colocar o texto 
    gameover_superficie = fonte.render('Sua pontuação foi : ' + str(pontos), True, vermelho)
    # criando um objeto retangular pro texto de gameover
    gameover_rect = gameover_superficie.get_rect()
    # setando a posicao do texto
    gameover_rect.midtop = (tela_x/2, tela_y/4)
    # colocando o texto na tela
    janela.blit(gameover_superficie, gameover_rect)
    pygame.display.flip()

    time.sleep(1)
    pygame.quit()
    quit()
    

# GAMEPLAY
while True:
    # fazendo os movimentos da cobrinha
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if andar != 'baixo':
                    andar = 'cima'
            
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if andar != 'cima':
                    andar = 'baixo'
            
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if andar != 'direita':    
                    andar = 'esquerda'
            
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if andar != 'esquerda':
                    andar = 'direita'
    
    # nao pode andar em duas direções ao mesmo tempo
    if andar == 'cima' and andar != 'baixo':
        andar = 'cima'
    if andar == 'baixo' and andar != 'cima':
        andar = 'baixo'
    if andar == 'esquerda' and andar != 'direita':
        andar = 'esquerda'
    if andar == 'direita' and andar != 'esquerda':
        andar = 'direita'

    # fazendo a cobrinha andar 
    if andar == 'cima':
        cobra_pos[1] -= 10

    if andar == 'baixo':
        cobra_pos[1] += 10

    if andar == 'esquerda':
        cobra_pos[0] -= 10
 
    if andar == 'direita':
        cobra_pos[0] += 10
    
    # fazendo a cobrinha crescer
    # se a cobrinha colidir com alguma fruta a pontuação sobe
    cobra_corpo.insert(0, list(cobra_pos))
    if cobra_pos[0] == fruta_pos[0] and cobra_pos[1] == fruta_pos[1]:
        pontos += 1
        fruta_spawn = False
    else:
        cobra_corpo.pop()

    if not fruta_spawn:
        fruta_pos = [random.randrange(1, (tela_x//10)) * 10,
                     random.randrange(1, (tela_y//10)) * 10]
    
    fruta_spawn = True
    janela.fill(preto)

    for pos in cobra_corpo:
        pygame.draw.rect(janela, verde, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(janela, branco, pygame.Rect(fruta_pos[0], fruta_pos[1], 10, 10))

    # condições para gameover
    if cobra_pos[0] < 0 or cobra_pos[0] > tela_x-10:
        gameover()
    if cobra_pos[1] < 0 or cobra_pos[1] > tela_y-10:
        gameover()
    
    #colidindo com o proprio corpo
    for bloco in cobra_corpo[1:]:
        if cobra_pos[0] == bloco[0] and cobra_pos[1] == bloco[1]:
            gameover()
    

    # mostrando o score
    mostra_pontuacao(1, branco, 'comicsansms', 20)

    pygame.display.update()

    fps.tick(cobra_vel)
    