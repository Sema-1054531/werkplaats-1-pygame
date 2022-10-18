# import
import pygame
import random
from random import randrange

# initialise pygame
pygame.init()

# screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# background
background = pygame.image.load('background.png')

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# multiple enemies
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/meteor.png'))
    enemyX.append(736)
    enemyY.append(random.randrange(screen_height))
    enemyX_change.append(-1.5)
    enemyY_change.append(-1.5)

# enemy function
def add_enemy_at_location(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# game loop
running = True
while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy_x_pos += enemy_speed
        if enemy_speed >0:
            if enemy_x_pos >= screen_width:
                enemy_x_pos = 0
                enemy_y_pos = randrange(screen_height)

        if enemy_speed <0:
            if enemy_x_pos <= 0:
                enemy_x_pos = 800
                enemy_y_pos = randrange(screen_height)

        screen.blit(background, (0, 0))
        add_enemy_at_location(enemy_x_pos, enemy_y_pos)
        pygame.display.update()


    # background image
    screen.blit(background, (0, 0))

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move enemies
    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]
        if enemyX_change[i] > 0:
            if enemyX[i] >= screen_width:
                enemyX[i] = 0
                enemyY[i] = randrange(screen_height)

        if enemyY_change[i] < 0:
            if enemyX[i] <= 0:
                enemyX[i] = 800
                enemyY[i] = randrange(screen_height)

        # fuction call enemy
        add_enemy_at_location(enemyX[i], enemyY[i], i)

    # update
    pygame.display.update()

