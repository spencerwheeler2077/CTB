import main
import pygame
import pygame_widgets


def start():
    pygame.init()
    pygame.font.init()
    WHITE = (250, 250, 250)

    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Start menu")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Start", True, (0, 0, 0))
        textPos = (10, 10)
        background.blit(text, textPos)

    screen.blit(background, (0, 0))
    pygame.display.flip()


    going = True
    while going:
        screen.blit(background, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
                pygame.quit()


    main.main(3)



if __name__ == "__main__":
    start()
