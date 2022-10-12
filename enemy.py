# imports
import math
import random
import pygame

pygame.init()

# Background
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load('background.png')

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/meteor.png'))
    enemyX.append(random.randint(100, 736))
    enemyY.append(random.randrange(0, 540))
    enemyX_change.append(20)
    enemyY_change.append(2)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY):
    distance = math.sqrt(math.pow(enemyX, 2) + (math.pow(enemyY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Game loop
running = True
while running:

    #RGB RED,GREEN,BLEU (kleur)
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Enemy movement
    for i in range(num_of_enemies):

        enemyY[i] += enemyY_change[i]
        if enemyY[i] <= 0:
            enemyY_change[i] = 2
            enemyX[i] += enemyX_change[i]
        elif enemyY[i] >= 540:
            enemyY_change[i] = -2
            enemyX[i] += enemyX_change[i]


        # Collision
        collision = isCollision(enemyX[i], enemyY[i])
        if collision:
            enemyX[i] = random.randint(10, 736)
            enemyY[i] = random.randint(0, 540)

        enemy(enemyX[i], enemyY[i], i)

    pygame.display.update()