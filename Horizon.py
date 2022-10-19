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

def player(x,y):
    screen.blit(playerImg, (x, y))

#Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

