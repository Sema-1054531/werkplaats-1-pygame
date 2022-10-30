import pygame
from pygame import mixer
import sys
import math
import random

#init pygame modules
pygame.init()

#screen 
width = 800
height = 600

#window
screen = pygame.display.set_mode((width, height))

#caption
pygame.display.set_caption("Space Shooter | Ware-IT" )

#font
font = "8-Bit-Madness.ttf"

#text rendering function
def message_to_screen(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, 0, color)

    return my_message

#player 
pygame.display.set_icon(pygame.image.load("images/newship2.png"))

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

#colors
cyan = (0,255,255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169,162,157)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#framerate
clock = pygame.time.Clock()
FPS = 60

#main menu
def main_menu():
    menu = True

    selected = "play"

    while menu:
    #controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    # pygame.mixer.Sound.play(select)
                    selected = "play"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    # pygame.mixer.Sound.play(select)
                    selected = "quit"
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    # pygame.mixer.Sound.play(select2)
                    if selected == "play":
                        menu = False
                    if selected == "quit":
                        pygame.quit()
                        quit()

        #drawing background
        screen.fill(black)

        for i in range(num_of_star):
            star[i].draw_stars()
            star[i].xcor += star[i].xchange

            if star[i].xcor <= 0:
                star[i].xcor = width
                star[i].ycor = random.randint(2, height)

        title = message_to_screen("Space Ware-it", font, 100, white)
        controls_1 = message_to_screen("", font, 30, white)
        controls_3 = message_to_screen("WARE-IT", font, 30, white)
        if selected == "play":
            play = message_to_screen("PLAY GAME", font, 75, white)
        else:
            play = message_to_screen("PLAY GAME", font, 75, gray)
        if selected == "quit":
            game_quit = message_to_screen("QUIT GAME", font, 75, white)
        else:
            game_quit = message_to_screen("QUIT GAME", font, 75, gray)

        title_rect = title.get_rect()
        controls_1_rect = controls_1.get_rect()
        controls_3_rect = controls_3.get_rect()
        play_rect = play.get_rect()
        quit_rect = game_quit.get_rect()

        #drawing text
        screen.blit(title, (width/2 - (title_rect[2]/2), 100))
        screen.blit(controls_1, (width/2 - (controls_1_rect[2]/2), 200))
        screen.blit(controls_3, (width/2 - (controls_3_rect[3]-300), 550))
        screen.blit(play, (width/2 - (play_rect[2]/2), 240))
        screen.blit(game_quit, (width/2 - (quit_rect[2]/2), 320))

        #update portions of the screen 
        pygame.display.update()

        clock.tick(60)

#main function
def run_game():

    fps = 60  
    clock = pygame.time.Clock()

    #player class
    class Player: 
        def __init__(self, xcor, ycor, xchange, ychange, angle, image):
            self.xcor = xcor # 64
            self.ycor = ycor # 300
            self.xchange = xchange
            self.ychange = ychange
            self.angle = angle
            self.image = image
            
        def draw_image(self):
            screen.blit(pygame.transform.rotate(
                self.image, self.angle), (self.xcor, self.ycor))

            #check for border collision
            if self.ycor < 0:
                self.ycor = 0
                self.ychange = 0
            
            elif self.ycor > 550 :
                self.ycor = 550    
                self.ychange = 0
            
            if self.xcor < 0:
                self.xcor = 0
                self.xchange = 0
        
            elif self.xcor > 200:
                self.xcor = 200
                self.xchange = 0

     
    #score variable
    score = 0
    highscore_file = open('highscore.dat', "r")
    highscore_int = int(highscore_file.read())

    #player position
    player = Player(64, height / 2, 0, 0, 0,
    pygame.image.load("images/newship2.png"))  

    #movement speed
    movement_speed = 3

    #bullet class
    class Bullet():    
        def __init__(self, xcor, ycor, xchange, angle, image, fired):
            self.xcor = xcor
            self.ycor = ycor
            self.xchange = xchange        
            self.angle = angle
            self.image = image
            self.fired = fired

        def draw_image(self):
            screen.blit(pygame.transform.rotate(
                self.image, self.angle), (self.xcor, self.ycor))

    limit_bullet = 1
    bullets = []

    #making the object inside the list
    for i in range(limit_bullet):  
        bullets.append(Bullet(width, height, 0, player.angle,
                                pygame.image.load("bullet.png"), False))
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
               
    num_of_star = 95
    star = []
    for i in range(num_of_star):
        star.append(Stars(random.randint(2, width), random.randint(2, height), random.randint(2, movement_speed + 4) * -1,
                            random.randint(1, 3)))
    #enemy class
    class Enemies:
        def __init__(self, xcor, ycor, xchange, angle, image, ychange):
            self.xcor = xcor
            self.ycor = ycor
            self.xchange = xchange
            self.angle = angle
            self.image = image
            self.ychange = ychange

        def draw_image(self):
            screen.blit(pygame.transform.rotate(
                self.image, self.angle), (self.xcor, self.ycor))

    num_of_enemies = 5
    enemy = []
    enemy_img = ["images/meteor.png" for i in range(1, 11)]
    for i in range(num_of_enemies):
        enemy.append(Enemies(width + random.randint(width / 2, width), random.randint(1, height), random.randint(2, movement_speed + 3) * -1, 360,
                            pygame.image.load(random.choice(enemy_img)), random.choice([-1, 1])))
    
    #enemy collision check
    def collision(a, b, c, d, range):
        distance = math.sqrt((math.pow(a - c, 2)) +
                                (math.pow(b - d, 2))) <= range
        #check positioning
        print(a) # player.xcor 
        print(b) # player.ycor

        return distance

    #game loop       
    game_over = False
    game_over_state = False

    while True:
        #speed player
        movement_speed = (score // 10) + 5
        while game_over:

            screen.fill(black)

            for i in range(num_of_star):
                star[i].draw_stars()
                star[i].xcor += star[i].xchange

                if star[i].xcor <= 0:
                    star[i].xcor = width
                    star[i].ycor = random.randint(2, height)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #quit game
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN:
                    #play again
                    if event.key == pygame.K_p:
                        main_menu()
                        run_game()
                        
            #draw game_over text      
            if game_over_state:

                game_over = message_to_screen("GAME OVER", font, 100, white)
                score_draw = message_to_screen(f"SCORE: {score}", font, 65, white)
                hi_score = message_to_screen(f"HI-SCORE: " + str(highscore_int), font, 65, white)
                play_again = message_to_screen("(P) Play Again", font, 65, white)
                quit_game = message_to_screen("(Q) Quit Game", font, 65, white)

                game_over_rect = game_over.get_rect()
                score_draw_rect = score_draw.get_rect()
                hi_score_rect = hi_score.get_rect()
                play_again_rect = play_again.get_rect()
                quit_game_rect = play_again.get_rect()

                screen.blit(game_over, (width/2 - (game_over_rect[2]/2), 70))
                screen.blit(score_draw, (width/2 - (score_draw_rect[2]/2), 160))
                screen.blit(hi_score, (width/2 - (hi_score_rect[2]/2), 240))
                screen.blit(play_again, (width/2 - (play_again_rect[2]/2), 320))
                screen.blit(quit_game, (width/2 - (quit_game_rect[2]/2), 400))

                pygame.display.update()
            
                clock.tick(60)
        
        clock.tick(fps)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if score > highscore_int:
                    highscore_file = open('highscore.dat', "w")
                    highscore_file.write(str(score))
                    highscore_file.close()
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                
                # keyboard controls
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.ychange = -movement_speed      
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.ychange = movement_speed
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:          
                    player.xchange = movement_speed
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.xchange = -movement_speed

                # player bullet
                if event.key == pygame.K_SPACE and not bullets[-1].fired:
                    for i in range(limit_bullet):
                        bullets[i].xcor = player.xcor
                        bullets[i].ycor = (player.ycor + 25) + i * 27
                        bullets[i].fired = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.ychange = 0         
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.ychange = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.xchange = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.xchange = 0

        # draw stars
        for i in range(num_of_star):
            star[i].draw_stars()
            star[i].xcor += star[i].xchange

            if star[i].xcor <= 0:
                star[i].xcor = width
                star[i].ycor = random.randint(2, height)

        # player bullet
        for i in range(limit_bullet):
            if bullets[i].fired:
                bullets[i].xchange = movement_speed + 20
                bullets[i].xcor += bullets[i].xchange
                bullets[i].draw_image()

            if bullets[i].xcor >= width:
                bullets[i].fired = False
                bullets[i].xchange = 0
                bullets[i].xcor = width
                bullets[i].ycor = height

            # show enemy
            for i in range(num_of_enemies):
                enemy[i].xcor += enemy[i].xchange
                enemy[i].ycor += enemy[i].ychange
                enemy[i].draw_image()

                if enemy[i].ycor >= height - 64 or enemy[i].ycor <= 0:
                    enemy[i].ychange *= -1

                # enemy passed the player
                if enemy[i].xcor <= -64:   
                    game_over = True
                    game_over_state = True

                # 64 - game over condition hit by enemy 
                if collision(player.xcor, player.ycor, enemy[i].xcor, enemy[i].ycor, 40):
                    game_over_state = True          
                    game_over = True
                    
                # 800 - collision check player bullet and enemy
                for j in range(limit_bullet):  
                    if collision(bullets[j].xcor, bullets[j].ycor, enemy[i].xcor, enemy[i].ycor, 32):
                        score += 1
                        enemy[i].xcor = width
                        enemy[i].ycor = random.randint(1, height - 64)
                        enemy[i].xchange = random.randint(
                            1, movement_speed - 3) * -1
                        enemy[i].image = pygame.image.load(
                            random.choice(enemy_img))
                        bullets[j].fired = False
                        bullets[j].xchange = 0
                        bullets[j].xcor = width
                        bullets[j].ycor = height

        #draw ship
        player.draw_image()
        player.ycor += player.ychange
        player.xcor += player.xchange
        
        #draw score
        screen.blit(message_to_screen("SCORE: {0}".format(score), font, 35, white), (10, 10))

        # draw high score
        if score < highscore_int:
            hi_score_message = message_to_screen("HI-SCORE: {0}".format(highscore_int), font, 40, white)
        else:
            highscore_file = open('highscore.dat', "w")
            highscore_file.write(str(score))
            highscore_file.close()
            highscore_file = open('highscore.dat', "r")
            highscore_int = int(highscore_file.read())
            highscore_file.close()
            hi_score_message = message_to_screen("HI-SCORE: {0}".format(highscore_int), font, 40, white)

        hi_score_message_rect = hi_score_message.get_rect()

        screen.blit(hi_score_message, (800-hi_score_message_rect[2]-10, 10))

        #update the screen
        pygame.display.update()

main_menu()

run_game()


        
