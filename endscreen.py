import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#initialize a window or screen for display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#menu caption
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#score variable
score = 0

#define fonts
font = pygame.font.Font("8-Bit-Madness.ttf", 75)

#define colours
TEXT_COL = (255, 255, 255)
cyan = (0,255,255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (169,162,157)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(230, 325, resume_img, 1)
quit_button = button.Button(230, 420, quit_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw text
      draw_text("GAME OVER ", font, TEXT_COL, 225, 100)
      #draw score
      draw_text("SCORE: " + str(score), font, TEXT_COL, 225, 200)
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      #draw quit button
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if back_button.draw(screen):
        menu_state = "main"
  else:
    #draw text
    draw_text("this is the game_loop", font, TEXT_COL, 75, 250)
    draw_text("hit SPACE", font, TEXT_COL, 75, 300)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

# update screen
  pygame.display.update()
#close pygame
pygame.quit()