import pygame
import button

pygame.init()

#Create game window
screen_width = 800
screen_height = 600
playbutton_width = 176
playbutton_heigt = 84
quitbutton_width = 184
quitbutton_height = 84

#define font
def create_font(t, s=40, c=(255, 255, 255), b=False, i=False):
    font = pygame.font.Font("8-bit-madness.ttf", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text

name_text = create_font("Space Shooter")
startup_text = create_font("Press ENTER to continue")
groupname_text = create_font("Ware it")

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

#game variables
game_menu = False
menu_state = "main"


#define colours
TEXT_COL = (255, 255, 255)

#load button images
start_img = pygame.image.load("../pythonProject2/Images/Play.png").convert_alpha()
quit_img = pygame.image.load("../pythonProject2/Images/Quit.png").convert_alpha()

#Create button instances
start_button = button.Button(screen_width * 0.33 - playbutton_width // 2, screen_height * 0.15, start_img, 0.75)
quit_button = button.Button(screen_width * 0.66 - quitbutton_width // 2, screen_height * 0.15, quit_img, 0.75)

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
                if menu_state == "running":
                    import Gamewareit
            if quit_button.draw(screen):
                run = False

    else:
        name_text_rect = name_text.get_rect(center=(screen_width // 2, screen_height // 5))
        startup_text_rect = startup_text.get_rect(center=(screen_width // 2, screen_height // 1.75))
        groupname_text_rect = groupname_text.get_rect(center=(screen_width * 0.9, screen_height // 1.05))

        screen.blit(startup_text, startup_text_rect)
        screen.blit(name_text, name_text_rect)
        screen.blit(groupname_text, groupname_text_rect)

# event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_menu = True

        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()