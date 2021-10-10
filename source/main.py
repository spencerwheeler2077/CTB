import pygame
pygame.init()
white = (255, 255, 255)

x = 1500
y = 830
display_surface = pygame.display.set_mode((x, y))

image = pygame.image.load("resource/ChristmasTheBoardGame-pythonversion.png")

image = pygame.transform.scale(image, (x, y))

pygame.display.set_mode((x, y))
pygame.display.set_caption('map')


while True:
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()

