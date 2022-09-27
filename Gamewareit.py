import random

import pygame

pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')
# Title and Icon
pygame.display.set_caption("Space Ware IT")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#Player
playerImg = pygame.image.load('space.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('rock.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40

#Bullet
bulletImg = pygame.image.load('bully.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

#Game loop
running = True
while running:

    #RGB RED,GREEN,BLEU (kleur)
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit (background,(0,0))
    playerX -= 0
    print(playerX)
    for event in  pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

    # keystroke checking left or right.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_SPACE:
            bulletX = playerX
            fire_bullet(playerX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0


    # 5 = 5 + -0.1 - 5 = 5 - 0.1

    playerX += playerX_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

# checking for boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
#movement bounce enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    #bullet movement
    if bullet_state == "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change




