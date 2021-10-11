import pygame
import Pawn
import DestinationFactory
import Player

pygame.init()
white = (255, 255, 255)

x = 1500
y = 830
display_surface = pygame.display.set_mode((x, y))

background = pygame.image.load("resource/ChristmasTheBoardGame-pythonversion.png")

background = pygame.transform.scale(background, (x, y))

pygame.display.set_mode((x, y))
pygame.display.set_caption('Christmas the Board Game')

pawnImages = ['resource/yellowpawn.png', 'resource/bluepawn.png', 'resource/greenpawn.png', 'resource/whitepawn.png',
              'resource/orangepawn.png', 'resource/redpawn.png']

allSprites = pygame.sprite.RenderPlain()
playerList = []
for i in pawnImages:
    newPlayer = Player.Player(i, DestinationFactory.NorthPole)
    allSprites.add(newPlayer.pawn)
    playerList.append(newPlayer)




while True:

    display_surface.fill(white)
    display_surface.blit(background, (0, 0))
    allSprites.draw(display_surface)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()

