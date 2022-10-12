# import
import pygame
import os
import time
import random

# Background
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Enemies
METEOR = pygame.image.load("images/meteor.png")

class Enemy:
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6



# Main loop
def main():
    run = True

    while run:
        # Quit pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
main()