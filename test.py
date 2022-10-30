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

# player img
playerImg = pygame.image.load('newship.png')

# Bullet
bulletImg = pygame.image.load('bully.png')

# enemy
enemyImg = pygame.image.load('meteor.png')

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

# Bullet
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bulletImg = bulletImg
        self.x_change = 6
        self.y_change = 10
        self.state = "ready"

    def draw(self, screen):
        screen.blit(self.bulletImg, (self.x + 60, self.y + 15))

    def move(self, vel):
        self.x += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

# Player
class Player:
    COOLDOWN = 30

    def __init__(self, x, y, live=1):
        self.x = x
        self.y = y
        self.live = live
        self.playerImg = playerImg
        self.bulletImg = bulletImg
        self.bullets = []
        self.cool_down_counter = 0

    def draw(self, screen):
        screen.blit(self.playerImg, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)

    def move_bullets(self, vel, obj):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(height):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.live -= 1
                self.bullets.remove(bullet)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def fire_bullet(self):
        if self.cool_down_counter == 0:
            bullet = Bullet(self.x, self.y)
            self.bullets.append(bullet)
            self.cool_down_counter = 1

    def get_width(self):
        return self.playerImg.get_width()

    def get_height(self):
        return self.playerImg.get_height()

class Enemy:
    def __init__(self, x, y, velx, vely, live=1):
        self.x = x
        self.y = y
        self.live = live
        self.enemyImg = enemyImg
        self.velx = velx
        self.vely = vely

    def move(self, vel):
        self.x += vel

    def add_enemy_at_location(self,screen):
        screen.blit(self.enemyImg, (self.x, self.y))


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

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

# score
score = 0
highscore_file = open('highscore.dat', "r")
highscore_int = int(highscore_file.read())


# text rendering function
def show_text(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, 0, color)

    return my_message


# Game loop

highscore_file
highscore_int

def main():
    running = True
    FPS = 30

    playerX_change = 0
    playerY_change = 0

    bullet_vel = 6

    player = Player(70, 300)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        screen.blit(background, (0, 0))

        # draw score
        screen.blit(show_text("SCORE: {0}".format(score), font, 35, white), (10, 10))


        for enemy in enemies:
            enemy.add_enemy_at_location(screen)

        player.draw(screen)

        if lost:
            screen.blit(show_text("GAME OVER", font, 35, white), (2, 250))

        pygame.display.update()


    while running:
        clock.tick(FPS)
        redraw_window()

        enemies = []
        enemy_vel = -3
        num_of_enemies = 6

        if player.live <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                running = False
            else:
                continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if score > highscore_int:
                #     highscore_file = open('highscore.dat', "w")
                #     highscore_file.write(str(score))
                #     highscore_file.close()
                quit()

        # keystroke checking left or right.
        # keystate = pygame.key.get_pressed()
        #     if keystate[pygame.K_LEFT]:
        #         playerX_change = -5
        #         print("links")
        #     if keystate[pygame.K_RIGHT]:
        #         playerX_change = 5
        #         print("rechts")
        #     if keystate[pygame.K_DOWN]:
        #         playerY_change = 5
        #         print("omlaag")
        #     if keystate[pygame.K_UP]:
        #         playerY_change = -5
        #         print("omhoog")

    # movement eneymy
    # for i in range(num_of_enemies):
    #     enemies[i].add_enemy_at_location()
    #     enemies[i].enemyX += enemies[i].enemyX_change
    #     if enemies[i].enemyX_change > 0:
    #         if enemies[i].enemyX >= width:
    #             enemies[i].enemyX = 0
    #             enemies[i].enemyY = randrange(height)
    #
    #     if enemies[i].enemyY_change < 0:
    #         if enemies[i].enemyX <= 0:
    #             enemies[i].enemyX = 800
    #             enemies[i].enemyY = randrange(height)

        for i in range(num_of_star):
            star[i].draw_stars()
            star[i].xcor += star[i].xchange
            if star[i].xcor <= 0:
                star[i].xcor = width
                star[i].ycor = random.randint(2, height)


        # draw high score
        # if score < highscore_int:
        #     hi_score_message = show_text("HI-SCORE: {0}".format(highscore_int), font, 35, white)
        # else:
        #     highscore_file = open('highscore.dat', "w")
        #     highscore_file.write(str(score))
        #     highscore_file.close()
        #     highscore_file = open('highscore.dat', "r")
        #     highscore_int = int(highscore_file.read())
        #     highscore_file.close()
        #     hi_score_message = show_text("HI-SCORE: {0}".format(highscore_int), font, 35, white)
        #
        # hi_score_message_rect = hi_score_message.get_rect()
        #
        # screen.blit(hi_score_message, (800 - hi_score_message_rect[2] - 10, 10))

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

quit()