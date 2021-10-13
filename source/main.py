import pygame
import pygame_widgets
import DestinationFactory
import Player
from myButton import CTBGButton as Button

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

# setting the control panel up for players.
pygame.draw.rect(background, (0, 0, 0), (845, 5, 650, 190))
pygame.draw.rect(background, (198, 218, 200), (847, 7, 646, 186))

buttonX = 850
buttonTop = 25
buttonWidth = 225
buttonHeight = 30
buttonDif = 40
buttonList = []

def test(number):
    if number == 1:
        pygame.event.post(Event1)
    if number == 2:
        pygame.event.post(Event2)
    if number == 3:
        pygame.event.post(Event3)
    if number == 4:
        pygame.event.post(Event4)



for i in range(4):

    button = Button(background, buttonX, buttonTop + (buttonDif*i), buttonWidth, buttonHeight, i+1)
    button.setOnClick(test, [button.number])
    buttonList.append(button)

add1Button = Button(background, 1100, 100, 50, 50)


def updateControlPanel(numPlayer, List):

    Pointers = numPlayer.location.pointers
    for k in range(4):
        if len(Pointers) > k:
            List[k].setString(Pointers[k].giveName())
        else:
            List[k].setString("")


Event1 = pygame.event.Event(pygame.USEREVENT, attr1='DES1')
Event2 = pygame.event.Event(pygame.USEREVENT, attr1='DES2')
Event3 = pygame.event.Event(pygame.USEREVENT, attr1='DES3')
Event4 = pygame.event.Event(pygame.USEREVENT, attr1='DES4')




pygame.font.init()

Destination1 = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = Destination1.render("TEXT", False, (0, 0, 0))
background.blit(textsurface, (0, 0))
i = 0
Player = playerList[i]
updateControlPanel(Player, buttonList)
while True:

    display_surface.fill(white)
    display_surface.blit(background, (0, 0))
    allSprites.draw(display_surface)

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT:
            if event.attr1 == 'DES1':
                Player.goTo(Player.location.getDirection(0))
                updateControlPanel(Player, buttonList)
            if event.attr1 == 'DES2':
                Player.goTo(Player.location.getDirection(1))
                updateControlPanel(Player, buttonList)
            if event.attr1 == 'DES3':
                Player.goTo(Player.location.getDirection(2))
                updateControlPanel(Player, buttonList)
            if event.attr1 == 'DES4':
                Player.goTo(Player.location.getDirection(3))
                updateControlPanel(Player, buttonList)




    pygame_widgets.update(events)
    pygame.display.update()
