import pygame 
import modulos
from pygame.locals import *
import sys

def movimento_do_lixo():
    for i in range(len(espaco_lixo)):
        if espaco_lixo[i] != [0, 0]:
            espaco_lixo[i][1] += 1
            screen.blit(lixo, [espaco_lixo[i][0], espaco_lixo[i][1]])

    
def end():
    
    l = False 
    # lixo tocando no chao 
    for i in range (len(espaco_lixo)):
       if espaco_lixo[i][1] + 60 > 600:
           l = True

    #lixo tocando na nave
    Nave = (nave_x, 480, 120, 120 )
    for lixox, lixoy in espaco_lixo:
        lixo1 = (lixox, lixoy, 60, 60)
        if modulos.collision(Nave, lixo1):
            l =  True
            break
    return l

def tela_displayer():
    #loop display
    while True:   #serve para mudar os cenarios no game 
        event = pygame.event.poll() # pegar um eventos i/o
        if event.type == QUIT: # QUIT = metodo
            pygame.quit()  # encerrar todos o programa (todos os modulos do pygame)
            sys.exit()     # fecha a tela; quit = funcao q encerra de fato
        if event.type == KEYDOWN:
            if event.key == K_UP: 
                break
        if end():
            screen.blit(telal,(0, 0))
        elif t == 100:
            screen.blit(telaw,(0, 0))
        else:
            screen.fill((0,255,0))
            screen.blit(telai, (0, 0))
        pygame.display.flip()

pygame.init()  
font   = pygame.font.SysFont("comicsansms", 30) # fonte do marcador do placar da pontuaçação   
t      = 0 
pontos = 0 
nave_x = 340 
muni   = [[0, 0], [0, 0], [0, 0]] 
tela   = pygame.image.load("imagens/tela800X600.png")
telaw  = pygame.image.load("imagens/telaw.png")
telal  = pygame.image.load("imagens/telal.png")
telai  = pygame.image.load("imagens/init.png")
music  = pygame.mixer.Sound("sounds/jogo.ogg")
jato   = pygame.image.load("imagens/jato120X120.png")
tiro   = pygame.image.load("imagens/bala20X40.png")
lixo   = pygame.image.load("imagens/lixo60X60.png")
time   = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Reciclagem Selvagem...")
espaco_lixo = []
modulos.lixo_show(espaco_lixo)
music.play()
tela_displayer()
while True:  
    time.tick(60)
    event = pygame.event.poll()
    if event.type == QUIT: 
        break 

    # movimento em x com a nave
    tecla = pygame.key.get_pressed() # pressiona a nave 
    if tecla[K_RIGHT] == 1 and nave_x + 120 < 800:
        nave_x += 5
    if tecla[K_LEFT] == 1 and nave_x > 0:
        nave_x -= 5
    
    #tiro nave
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            for i in range(len(muni)):
                if muni[i] == [0, 0]:
                   muni[i] = [nave_x + 50, 450] # altura onde o tiro  sai da nave    
                   break
     
    # colisao com o tiro 
    for i in range(len(muni)):
        if muni[i] != [0, 0]:
            municao = (muni[i][0], muni[i][1], 20, 40)
            j = 0
            for lixox, lixoy in espaco_lixo:
                if lixox != 0 and lixoy != 0:
                    lixo1 = (lixox, lixoy, 60, 60)
                    if modulos.collision(municao, lixo1):
                        t += 1
                        muni[i] = [0, 0]
                        espaco_lixo[j] = [0, 0]
                        pontos += 1 
                j += 1
    
    # colisao tiro com a borda horzontal
    for i in range(len(muni)):
         if muni[i] != [0, 0]:
            if muni[i][1] < 0:
                muni[i] = [0, 0]
    
    
    screen.blit(tela, (0, 0))

    # movimento do lixo
    movimento_do_lixo()
    # movimento da bala 
    for i in range(len(muni)): 
        if muni[i] != [0, 0]:
            screen.blit(tiro, [muni[i][0], muni[i][1]])
            muni[i][1] -= 10

    screen.blit(jato,[nave_x, 480])
     
    if end() or t == 100:
        tela_displayer()

        espaco_lixo = [] # zeramos as posicoes pois precisamos reiniciando o jogo
        modulos.lixo_show(espaco_lixo) # retomamos as posicoes do inicio 
        t = 0 # zeramos as "colisoes"

        tela_displayer()
    # Placar de pontos
    text = font.render("PONTUAÇÃO: " + str(pontos) + "%", True, (255, 255, 255))
    screen.blit(text, (40, 40))

    pygame.display.flip()
