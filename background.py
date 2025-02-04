#Import pygame
import pygame
from pygame.locals import*
pygame.init()

#Creating a window
width = 800
height = 600
window = pygame.display.set_mode((800, 600))

#Background image
bg_img = pygame.image.load('../pythonProject2/Images/planet.jpg')
bg_img = pygame.transform.scale(bg_img, (width, height))

i = 0

#The loop
running = True
while running:

    #Blit function to avoid black screen
    window.fill((0,0,0))
    window.blit(bg_img, (i,0))
    window.blit(bg_img, (width+i,0))
    if (i==-width):
        window.blit(bg_img,(width+i,0))
        i=0
    i -= 0.4
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()
pygame.quit()




