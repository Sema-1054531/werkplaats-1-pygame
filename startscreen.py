import pygame
import button

pygame.init()

#Create game window
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

#game variables
game_menu = False
menu_state = "main"


#define fonts
font = pygame.font.SysFont("arialblack", 40)
font2 = pygame.font.SysFont("arialblack", 20)
#define colours
TEXT_COL = (255, 255, 255)

#load button images
start_img = pygame.image.load("images/Play.png").convert_alpha()
quit_img = pygame.image.load("images/Quit.png").convert_alpha()

#Create button instances
start_button = button.Button(125, 125, start_img, 1)
quit_button = button.Button(475, 125, quit_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#Game Loop
run = True
while run:

    screen.fill((0, 0, 0))

    #check if game is in the menu
    if game_menu == True:
        #check menu state
        if menu_state == "main":
            #draw menu screen buttons
            if start_button.draw(screen):
                menu_state = "running"
            if quit_button.draw(screen):
                run = False

    else:
        draw_text("Space Shooter", font, TEXT_COL, 230, 50)
        draw_text("Ware it", font2, TEXT_COL, 700, 550)
        draw_text("Press ENTER to continue", font2, TEXT_COL, 260, 200)


# event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_menu = True

        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()