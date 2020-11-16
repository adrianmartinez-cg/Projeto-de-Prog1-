import pygame
import random

#Inicializando o pygame e criando a janela com titulo e icone
pygame.init() #inicializa o pygame
screen=pygame.display.set_mode([800,600]) #cria uma janela com as dimensoes citadas, quando nos referirmos a janela, usaremos a variavel screen
pygame.display.set_caption("Space Invaders") #define titulo
icon=pygame.image.load("space/ufo.png") #define icone
pygame.display.set_icon(icon)

#Imagem de fundo
background=pygame.image.load('space/background.png')

# Jogador
playerImg=pygame.image.load('space/player.png')
playerX=370 #x inicial
playerY=480 #y inicial
playerX_change=0 #variavel que sera usada para dar movimento ao jogador

# Inimigo
enemyImg=pygame.image.load('space/enemy1.png')
enemyX=random.randint(0,700)
enemyY=random.randint(50,150)
enemyX_change=2 #ja inicia se movimentando
enemyY_change=40 #quando chegar as bordas ,desce 40 unidades para baixo

# Bala
# estado ready - Nao existe mais nenhuma bala na tela
# estado fire - A bala está atualmente se mexendo
bulletImg=pygame.image.load('space/bullet.png')
bulletX=0
bulletY=480
bulletY_change=10
bullet_state='ready'

def player(x,y):
    screen.blit(playerImg,(x,y)) #desenha a imagem do player na tela
def enemy(x,y):
    screen.blit(enemyImg,(x,y))
def fire_bullet(x,y):
    global bullet_state # acessa a variavel global bullet_state
    bullet_state= 'fire'
    screen.blit(bulletImg,(x+16,y+10)) # esses valores são para centralizar a bala

gameLoop=True # Variavel booleana para deixar o jogo rodando
while gameLoop:
    screen.fill([0,0,0]) #preenche a tela com alguma cor
    screen.blit(background,(0,0)) #preenche a tela com a imagem de fundo
    for event in pygame.event.get(): # Aqui iremos ver os eventos que estão acontecendo
        if event.type == pygame.QUIT: # Se clicarmos no botao de fechar
            gameLoop=False
        if event.type == pygame.KEYDOWN: # se alguma tecla foi pressionada (keyup = soltar tecla)
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change= 2
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP: # se soltarmos as teclas de movimento , para de mexer a nave
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0

    playerX+= playerX_change # atualiza o valor da coordenada X
    if playerX <= 0: # Para nao sair da janela do jogo
        playerX=0
    elif playerX >= 736:
        playerX=736

    enemyX+= enemyX_change 
    if enemyX <= 0:
        enemyX_change=2 #Quando chegar ao limite da esquerda da tela, ir para a direita
        enemyY+= enemyY_change
    elif enemyX >= 736:
        enemyX_change=-2
        enemyY+= enemyY_change
    # movimento da bala
    if bulletY <=0:
        bulletY=480
        bullet_state='ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY) # temos que desenhar constantemente o jogador e inimigo 
    enemy(enemyX,enemyY)
    pygame.display.update() #mantem a janela do jogo aberta
