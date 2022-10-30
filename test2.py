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

# player
playerImg = pygame.image.load('newship.png')

# player
enemyImg = pygame.image.load('meteor.png')

# Bullet
bulletImg = pygame.image.load('bully.png')

# Title and Icon
pygame.display.set_caption("Space Ware IT")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# font
font = "8-Bit-Madness.ttf"

# colors
cyan = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169, 162, 157)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


class Player:
    def __init__(self, playerX, playerY, playerX_change, playerY_change, live=1):
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = playerX_change
        self.playerY_change = playerY_change
        self.playerImg = playerImg
        self.live = live

    def player(self, screen):
        screen.blit(self.playerImg, (self.playerX, self.playerY))


class Enemy:
    def __init__(self, enemyX, enemyY, enemyX_change, enemyY_change, live=1):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change
        self.enemyY_change = enemyY_change
        self.enemyImg = enemyImg
        self.live = live

    def add_enemy_at_location(self, screen):
        screen.blit(self.enemyImg, (self.enemyX, self.enemyY))

class Bullet:
    def __init__(self, bulletX, bulletY):
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bulletImg = bulletImg
        self.bulletX_change = 6
        self.bulletY_change = 10
        self.bullet_state = "ready"

    def fire_bullet(self, screen):
        screen.blit(self.bulletImg, (self.bulletX + 60, self.bulletY + 15))


# framerate
clock = pygame.time.Clock()
FPS = 30

# score
score = 0
highscore_file = open('highscore.dat', "r")
highscore_int = int(highscore_file.read())


# text rendering function
def show_text(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, 0, color)

    return my_message

# star class
movement_speed = 3
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
num_of_enemies = 6
enemies = []
for i in range(num_of_enemies):
    enemy = Enemy(736, random.randrange(height), -3, -3)
    enemies.append(enemy)


def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Formula of collision distance between 2 points and midpoint
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:  # distance between left of the screen and airplane
        return True  # Collision had occur
    else:
        return False


# def show_text(msg, x, y, color, size):
#     font = pygame.font.Font("8-bit-madness.ttf", size)
#     text = font.render(msg, True, color)
#     screen.blit(text, (x, y))

# Game loop

highscore_file
highscore_int

running = True
while running:

    # RGB RED,GREEN,BLEU (kleur)
    screen.fill(black)

    for i in range(num_of_star):
        star[i].draw_stars()
        star[i].xcor += star[i].xchange
        if star[i].xcor <= 0:
            star[i].xcor = width
            star[i].ycor = random.randint(2, height)

    Player.playerX -= 0
    Player.playerY -= 0
    for event in pygame.event.get():
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
                Bullet.fire_bullet(bulletX, bulletY)
                if Bullet.bullet_state == "ready":
                    bulletSound = mixer.Sound("bulletsound.wav")
                    bulletSound.play()
                    bullet_state = "fire"

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0

    # 5 = 5 + -0.1 - 5 = 5 - 0.1

    Player.playerX += Player.playerX_change
    Player.playerY += Player.playerY_change
    Bullet.bulletX += Bullet.bulletX_change

    Player.player(playerX, playerY)

    # movement eneymy
    for i in range(num_of_enemies):
        enemies[i].add_enemy_at_location()
        enemies[i].enemyX += enemies[i].enemyX_change
        if enemies[i].enemyX_change > 0:
            if enemies[i].enemyX >= width:
                enemies[i].enemyX = 0
                enemies[i].enemyY = randrange(height)

        if enemies[i].enemyY_change < 0:
            if enemies[i].enemyX <= 0:
                enemies[i].enemyX = 800
                enemies[i].enemyY = randrange(height)

        # Bullet and Enemy Collision
        # inside 'for' loops, so it will count ALL enemies collision
        collision = isCollision(enemies[i].enemyX, enemies[i].enemyY, bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 10
            # enemy will respawn at random location
            enemies[i].enemyX = random.randint(750, 800)
            enemies[i].enemyY = random.randint(50, 150)

        Enemy.add_enemy_at_location(screen)

    # bullet movement
    if bullet_state == "fire":
        Bullet.fire_bullet(bulletX, bulletY)
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

    # draw score
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

    screen.blit(hi_score_message, (800 - hi_score_message_rect[2] - 10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()

quit()

