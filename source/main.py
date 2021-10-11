import pygame
import Pawn
pygame.init()
white = (255, 255, 255)

x = 1500
y = 830
display_surface = pygame.display.set_mode((x, y))

background = pygame.image.load("resource/ChristmasTheBoardGame-pythonversion.png")

background = pygame.transform.scale(background, (x, y))

pygame.display.set_mode((x, y))
pygame.display.set_caption('map')


pawn1 = Pawn.Pawn('resource/yellowpawn.png', (150, 250))
pawn2 = Pawn.Pawn('resource/bluepawn.png', (30, 50))
grid = Pawn.Grid('resource/grid.png')
allSprites = pygame.sprite.RenderPlain((pawn2, pawn1))

while True:

    display_surface.fill(white)
    display_surface.blit(background, (0, 0))
    allSprites.draw(display_surface)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()

