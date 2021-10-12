import pygame
import pygame_widgets
from pygame_widgets.button import Button
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

AdjustmentList = [[-9, -6], [-9, 6], [0, -6], [0, 6], [9, -6], [9, 6]]

allSprites = pygame.sprite.RenderPlain()
playerList = []
for i in range(6):
    newPlayer = Player.Player(pawnImages[i], DestinationFactory.Astana, AdjustmentList[i])
    allSprites.add(newPlayer.pawn)
    playerList.append(newPlayer)

pygame.draw.rect(background, (0, 0, 0), (845, 5, 650, 190))
pygame.draw.rect(background, (198, 218, 200), (847, 7, 646, 186))

buttonX = 850
buttonTop = 25
buttonWidth = 225
buttonHeight = 30
buttonDif = 40
buttonList = []

for i in range(4):
    buttonList.append(Button(background, buttonX, buttonTop + (buttonDif*i), buttonWidth, buttonHeight))

add1Button = Button(background, 1100, 100, 50, 50)


def updateControlPanel(numPlayer, List):

    Pointers = numPlayer.location.pointers
    for k in range(4):
        if len(Pointers) > k:
            List[k].setString(Pointers[k].giveName())
        else:
            List[k].setString("")


updateControlPanel(playerList[0], buttonList)


while True:
    display_surface.fill(white)
    display_surface.blit(background, (0, 0))
    allSprites.draw(display_surface)

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame_widgets.update(events)
    pygame.display.update()

