import pygame
import pygame_widgets
import DestinationFactory
import Player
from myButton import CTBGButton as Button

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont(None, 40)
WHITE = (255, 255, 255)

WINDOW_X = 1500
WINDOW_Y = 830
PANEL_COLOR = (198, 218, 200)

display_surface = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

background = pygame.image.load("resource/ChristmasTheBoardGame-pythonversion.png")
background = pygame.transform.scale(background, (WINDOW_X, WINDOW_Y))

pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption('Christmas the Board Game')

# variables to make the players
pawnImages = ['resource/yellowpawn.png', 'resource/bluepawn.png', 'resource/greenpawn.png', 'resource/whitepawn.png',
              'resource/orangepawn.png', 'resource/redpawn.png']
AdjustmentList = [[-9, -6], [-9, 6], [0, -6], [0, 6], [9, -6], [9, 6]]
allSprites = pygame.sprite.RenderPlain()
playerList = []

for i in range(6):
    newPlayer = Player.Player(f"Player {i+1}", pawnImages[i], DestinationFactory.NorthPole, AdjustmentList[i])
    allSprites.add(newPlayer.pawn)
    playerList.append(newPlayer)


# setting the control panel up for players.
PANEL_X = 845
PANEL_Y = 5
PANEL_LEN = 650
PANEL_HEIGHT = 190

pygame.draw.rect(background, (0, 0, 0), (PANEL_X, PANEL_Y, PANEL_LEN, PANEL_HEIGHT))
pygame.draw.rect(background, PANEL_COLOR, (PANEL_X + 3, PANEL_Y + 3, PANEL_LEN-4, PANEL_HEIGHT-4))

buttonX = PANEL_X + 5
buttonTop = PANEL_Y + 20
buttonWidth = 225
buttonHeight = 30
buttonDif = 40
buttonList = []


def desButtonpost(number):
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
    button.setOnClick(desButtonpost, [button.number])
    buttonList.append(button)

EndTurn = pygame.event.Event(pygame.USEREVENT, attr1='END')


def roll(player):

    player.roll()


def endButtonFunc():
    pygame.event.post(EndTurn)


endTurnButton = Button(background, PANEL_X + buttonWidth + 20, PANEL_Y + PANEL_HEIGHT - 40, 120, 35)
endTurnButton.setString("End Turn")
endTurnButton.setOnClick(endButtonFunc)

ROLL = pygame.event.Event(pygame.USEREVENT, attr1='ROLL')


def rollButtonFunc():
    pygame.event.post(ROLL)


def updateRollView(player, surface):
    surface.fill(PANEL_COLOR)
    text = FONT.render(f"{player.rollCount}", False, (0, 0, 0))
    surface.blit(text, surface.get_rect())
    background.blit(surface, (PANEL_X + buttonWidth + 30, PANEL_Y + 40))



rollView = pygame.Surface((50, 50))


rollButton = Button(background, PANEL_X + buttonWidth + 20, PANEL_Y + PANEL_HEIGHT - 80, 80, 35)
rollButton.setString("Roll")
rollButton.setOnClick(rollButtonFunc)

desButColDis = (100, 100, 100)
activeButtonCol = (220, 220, 220)
def updateDesButtons(numPlayer, List):

    Pointers = numPlayer.location.pointers
    for k in range(4):

        if len(Pointers) > k:
            List[k].setString(Pointers[k].giveName() + f' ({str(Pointers[k].giveDistance())})')
            if Pointers[k].giveDistance() > numPlayer.rollCount:
                List[k].disable()
                List[k].colour = desButColDis
            else:
                List[k].enable()
                List[k].colour = activeButtonCol

        else:
            List[k].setString("")
            List[k].disable()
            List[k].colour = (100, 100, 100)


def updateName(numPlayer, surface):
    surface.fill(PANEL_COLOR)
    text = FONT.render(f"{numPlayer.name}", False, (0, 0, 0))
    surface.blit(text, (0, 0))
    playerNameText.blit(surface, (0, 0))
    background.blit(surface, (PANEL_X + buttonWidth + 20, PANEL_Y + 10))



Event1 = pygame.event.Event(pygame.USEREVENT, attr1='DES1')
Event2 = pygame.event.Event(pygame.USEREVENT, attr1='DES2')
Event3 = pygame.event.Event(pygame.USEREVENT, attr1='DES3')
Event4 = pygame.event.Event(pygame.USEREVENT, attr1='DES4')


i = 0
Player = playerList[i]
updateDesButtons(Player, buttonList)
playerNameText = pygame.Surface((150, 30))  # these numbers here are the dimensions of the text surface
updateName(Player, playerNameText)


while True:

    display_surface.fill(WHITE)
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

            if event.attr1 == 'DES2':
                Player.goTo(Player.location.getDirection(1))

            if event.attr1 == 'DES3':
                Player.goTo(Player.location.getDirection(2))

            if event.attr1 == 'DES4':
                Player.goTo(Player.location.getDirection(3))

            if event.attr1 == 'END':
                Player.reset()
                playerList[i] = Player

                if i == 5:
                    i = -1

                i += 1
                Player = playerList[i]


            if event.attr1 == 'ROLL':
                roll(Player)


            updateDesButtons(Player, buttonList)
            updateName(Player, playerNameText)
            updateRollView(Player, rollView)

    pygame_widgets.update(events)
    pygame.display.update()
