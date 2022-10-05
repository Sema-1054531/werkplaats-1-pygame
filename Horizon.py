import random

import pygame

pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Ware IT")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('newship.png')
playerX = 70
playerY = 300
playerX_change = 0


#Game loop
