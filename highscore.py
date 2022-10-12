#score
score = 0


def show_text(msg, x, y, color, size):
    font = pygame.font.Font("8-bit-madness.ttf", size)
    text = font.render(msg, True, color)
    screen.blit(text, (x, y))

    show_text(f"SCORE: {score}", 10, 10, white, 35)
    pygame.display.update()
