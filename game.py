#Import library pygame
import pygame
pygame.init()

#Screen aanmaken
screen = pygame.display.set_mode((1000, 600))
background = pygame.image.load('images/spaceship.png')

#Titel game
pygame.display.set_caption('Space Ware IT')

#blit() om afbeelding op scherm te krijgen
screen.blit(background, (0, 0))

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Update scherm
    pygame.display.update()






