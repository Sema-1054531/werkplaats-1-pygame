import pygame
import random
from random import randrange

pygame.init()

# Background
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Enemies
METEOR = pygame.image.load("images/meteor.png")

# Background
background = pygame.image.load('background.png')


enemy_x_pos = 0
enemy_y_pos = random.randrange(screen_height)
enemy_speed = 3

def add_enemy_at_location(x, y):
    screen.blit(METEOR, (x, y))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    enemy_x_pos += enemy_speed
    if enemy_x_pos >= screen_width:
        enemy_x_pos = 0
        enemy_y_pos = randrange(screen_height)

    screen.blit(background, (0, 0))
    add_enemy_at_location(enemy_x_pos, enemy_y_pos)
    pygame.display.update()