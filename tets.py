# import random
# import pygame
#
# # create screen
# screen = pygame.display.set_mode((800, 600))
#
# #Enemy
# enemyImg = pygame.image.load('images/meteor.png')
# enemyX = random.randint(0, 800)
# enemyY = random.randint(50, 150)
# enemyX_change = 4
# enemyY_change = 40
#
# def enemy(x,y):
#     screen.blit(enemyImg, (x, y))
#
# #Game loop
# running = True
# while running:
#
#     for event in  pygame.event.get() :
#         if event.type == pygame.QUIT:
#             running = False
#
#     enemy(enemyX, enemyY)
#     pygame.display.update()
#
# #movement bounce enemy
#     enemyX += enemyX_change
#     if enemyX <= 0:
#         enemyX_change = 4
#         enemyY += enemyY_change
#     elif enemyX >= 736:
#         enemyX_change = -4
#         enemyY += enemyY_change

import pygame
from random import randrange