import random
import pygame


pygame.init()

# screen setup
width = 800
height = 600

# create screen
screen = pygame.display.set_mode((width, height))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Space Ware IT")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#font
font = pygame.font.Font('8-bit-madness.ttf', 100)

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
#Enemy
enemyImg = pygame.image.load('meteor.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40

#Bullet
bulletImg = pygame.image.load('bully.png')
bulletX = playerX
bulletY = playerY
bulletX_change = 3
bulletY_change = 10
bullet_state = "ready"
bullet = []

#score
score = 0
# highscore_file = open('highscore.dat', "r")
# highscore_int = int(highscore_file.read())

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x,y):
    screen.blit(bulletImg,(x + 60 ,y + 15))



def show_text(msg, x, y, color, size):
    font = pygame.font.Font("8-bit-madness.ttf", size)
    text = font.render(msg, True, color)
    screen.blit(text, (x, y))

#Game loop

# highscore_file
# highscore_int

running = True
while running:

    #RGB RED,GREEN,BLEU (kleur)
    screen.fill((0, 0, 0))
    #Background Image
    screen.blit (background,(0,0))
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
        if event.key == pygame.K_LSHIFT:
            bulletX = playerX
            bulletY = playerY
            fire_bullet(bulletX, bulletY)
            if bullet_state == "ready":
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
    enemy(enemyX, enemyY)

    #bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)


# checking for boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 550:
        playerY = 550

#movement bounce enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change


#bullet movement
    if bullet_state == "fire":
        fire_bullet(playerX,bulletY)
        bulletX += bulletX_change


# draw score
    show_text(f"SCORE: {score}", 10, 10, white, 35)

# draw high score
    # if score < highscore_int:
    #         hi_score_message = show_text("HI-SCORE: {0}".format(highscore_int), font, 50, black, 30)
    # else:
    #         highscore_file = open('highscore.dat', "w")
    #         highscore_file.write(str(score))
    #         highscore_file.close()
    #         highscore_file = open('highscore.dat', "r")
    #         highscore_int = int(highscore_file.read())
    #         highscore_file.close()
    #         hi_score_message = show_text("HI-SCORE: {0}".format(highscore_int), font, 50, yellow, 30)

    # hi_score_message_rect = hi_score_message.get_rect()

    # screen.blit(hi_score_message, (800-hi_score_message_rect[2]-10, 10))

    pygame.display.update()

pygame.quit()

quit()

