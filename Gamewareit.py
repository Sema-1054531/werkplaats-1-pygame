import pygame
import random
import math
from pygame import mixer
from random import randrange

pygame.init()

# screen setup
width = 800
height = 600

# create screen
screen = pygame.display.set_mode((width, height))

# Background
background = pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Ware IT")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#font
font = "8-Bit-Madness.ttf"

# colors
cyan = (0,255,255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169,162,157)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#Player
playerImg = pygame.image.load('newship.png')
playerX = 70
playerY = 300
playerX_change = 0
playerY_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

#Bullet
bulletImg = pygame.image.load('bully.png')
bulletX = playerX
bulletY = playerY
bulletX_change = 6
bulletY_change = 10
bullet_state = "ready"

# framerate
clock = pygame.time.Clock()
FPS = 30

#score
score = 0
highscore_file = open('highscore.dat', "r")
highscore_int = int(highscore_file.read())

# text rendering function
def show_text(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, 0, color)

    return my_message

movement_speed = 3

#star class
class Stars:   
    def __init__(self, xcor, ycor, xchange, width):
        self.xcor = xcor
        self.ycor = ycor
        self.xchange = xchange
        self.width = width

    def draw_stars(self):
        pygame.draw.rect(
            screen, white, (self.xcor, self.ycor, self.width, self.width))
        
num_of_star = 75
star = []
for i in range(num_of_star):
    star.append(Stars(random.randint(2, width), random.randint(2, height), random.randint(2, movement_speed + 4) * -1,
                        random.randint(1, 3)))


# multiple enemies
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('meteor.png'))
    enemyX.append(736)
    enemyY.append(random.randrange(height))
    enemyX_change.append(-3)
    enemyY_change.append(-3)

def player(x,y):
    screen.blit(playerImg, (x, y))

def add_enemy_at_location(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    screen.blit(bulletImg,(x + 60 ,y + 15))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Formula of collision distance between 2 points and midpoint
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 27: #distance between left of the screen and airplane
        return True # Collision had occur
    else:
        return False

# def show_text(msg, x, y, color, size):
#     font = pygame.font.Font("8-bit-madness.ttf", size)
#     text = font.render(msg, True, color)
#     screen.blit(text, (x, y))

#Game loop

highscore_file
highscore_int

running = True
while running:

    #RGB RED,GREEN,BLEU (kleur)
    screen.fill(black)

    for i in range(num_of_star):
        star[i].draw_stars()
        star[i].xcor += star[i].xchange
        if star[i].xcor <= 0:
            star[i].xcor = width
            star[i].ycor = random.randint(2, height)

    playerX -= 0
    playerY -= 0
    for event in  pygame.event.get() :
        if event.type == pygame.QUIT:
            if score > highscore_int:
                highscore_file = open('highscore.dat', "w")
                highscore_file.write(str(score))
                highscore_file.close()
            running = False


    # show_text(f"SCORED: {score}", width * 1 / 3, height * 4 / 5, white, 40)
    # keystroke checking left or right.

        # keystroke checking left or right.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                print("links")
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                print("rechts")
            if event.key == pygame.K_DOWN:
                playerY_change = 5
                print("omlaag")
            if event.key == pygame.K_UP:
                playerY_change = -5
                print("omhoog")
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("bulletsound.wav")
                    bulletSound.play()
                    bullet_state = "fire"
 


    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0

    # 5 = 5 + -0.1 - 5 = 5 - 0.1

    playerX += playerX_change
    playerY += playerY_change
    bulletX += bulletX_change


    player(playerX, playerY)
    # add_enemy_at_location(enemyX[i], enemyY[i], i)

    #movement eneymy
    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]
        if enemyX_change[i] > 0:
            if enemyX[i] >= width:
                enemyX[i] = 0
                enemyY[i] = randrange(height)

        if enemyY_change[i] < 0:
            if enemyX[i] <= 0:
                enemyX[i] = 800
                enemyY[i] = randrange(height)

        # Bullet and Enemy Collision
        # inside 'for' loops, so it will count ALL enemies collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 10
            # enemy will respawn at random location
            enemyX[i] = random.randint(750, 800)
            enemyY[i] = random.randint(50, 150)


        add_enemy_at_location(enemyX[i], enemyY[i], i)

    #bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
    # reset the bullet when it reachs the top of the screen, so the space ship can shoot multiple times
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

# checking for boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 550:
        playerY = 550



     #draw score
    screen.blit(show_text("SCORE: {0}".format(score), font, 35, white), (10, 10))

# draw high score
    if score < highscore_int:
        hi_score_message = show_text("HI-SCORE: {0}".format(highscore_int), font, 35, white)
    else:
        highscore_file = open('highscore.dat', "w")
        highscore_file.write(str(score))
        highscore_file.close()
        highscore_file = open('highscore.dat', "r")
        highscore_int = int(highscore_file.read())
        highscore_file.close()
        hi_score_message = show_text("HI-SCORE: {0}".format(highscore_int), font, 35, white)

    hi_score_message_rect = hi_score_message.get_rect()

    screen.blit(hi_score_message, (800-hi_score_message_rect[2]-10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()

quit()

