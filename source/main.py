import pygame
import pygame_widgets
import DestinationFactory
import Player as play
from myButton import CTBGButton as Button
import time


def main(numberOfPlayers, deckSize):

    pygame.init()
    pygame.font.init()

    FONT = pygame.font.SysFont("Timeless", 40)
    WHITE = (255, 255, 255)

    NUMPLAYERS = numberOfPlayers
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
    AdjustmentList = [[-11, -7], [-1, -7], [9, -7], [-9, 7], [1, 7], [11, 7]]
    allSprites = pygame.sprite.RenderPlain()
    playerList = []

    for i in range(NUMPLAYERS):
        newPlayer = play.Player(f"Player {i+1}", pawnImages[i], DestinationFactory.NorthPole,
                                AdjustmentList[i], deckSize)

        allSprites.add(newPlayer.pawn)
        playerList.append(newPlayer)


    # setting the control panel up for players.
    PANEL_X = 845
    PANEL_Y = 5
    PANEL_LEN = 650
    PANEL_HEIGHT = 190

    pygame.draw.rect(background, (0, 0, 0), (PANEL_X, PANEL_Y, PANEL_LEN, PANEL_HEIGHT))
    pygame.draw.rect(background, PANEL_COLOR, (PANEL_X + 3, PANEL_Y + 3, PANEL_LEN-6, PANEL_HEIGHT-6))

    buttonX = PANEL_X + 5
    buttonTop = PANEL_Y + 10
    buttonWidth = 225
    buttonHeight = 30
    buttonDif = 37
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

    HAND_FONT = pygame.font.SysFont("Timeless", 30)

    Complete = pygame.event.Event(pygame.USEREVENT, attr1='COMPLETE')

    Reset = pygame.event.Event(pygame.USEREVENT, attr1='RESET')


    def resetButtonFun():
        pygame.event.post(Reset)


    resetButton = Button(background, PANEL_X + buttonWidth - 60, PANEL_Y + PANEL_HEIGHT - 35, 60, 30)
    resetButton.setString("Go Back")
    resetButton.setOnClick(resetButtonFun)

    def finishButtonFun():

        pygame.event.post(Complete)
        pygame.event.post(EndTurn)


    finishButton = Button(background, PANEL_X + buttonWidth + 170, PANEL_Y + PANEL_HEIGHT - 30, 150, 25)
    finishButton.setString("Complete Destination")
    finishButton.setOnClick(finishButtonFun)


    def updateComplete(player):

        for j in range(3):
            if player.location.name == player.deck.hand[j]:
                finishButton.enable()
                return
            else:
                finishButton.disable()


    def updateDestinationView(player, surface):
        hand1 = player.deck.hand[0]
        hand2 = player.deck.hand[1]
        hand3 = player.deck.hand[2]
        location = player.location.name

        surface.fill((170, 140, 130))

        if hand1 == location:
            text1 = HAND_FONT.render(f"{hand1}", False, (0, 200, 0))
        else:
            text1 = HAND_FONT.render(f"{hand1}", False, (0, 0, 0))

        if hand2 == location:
            text2 = HAND_FONT.render(f"{hand2}", False, (0, 200, 0))
        else:
            text2 = HAND_FONT.render(f"{hand2}", False, (0, 0, 0))

        if hand3 == location:
            text3 = HAND_FONT.render(f"{hand3}", False, (0, 200, 0))
        else:
            text3 = HAND_FONT.render(f"{hand3}", False, (0, 0, 0))

        surface.blit(text1, (5, 10))
        surface.blit(text2, (5, 40))
        surface.blit(text3, (5, 70))
        background.blit(surface, (PANEL_X + PANEL_LEN - 275, PANEL_Y + 15))


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
    WIN = pygame.event.Event(pygame.USEREVENT, attr1='WIN')


    i = 0
    Player = playerList[i]
    updateDesButtons(Player, buttonList)
    playerNameText = pygame.Surface((150, 30))  # these numbers here are the dimensions of the text surface
    handView = pygame.Surface((270, 100))
    updateName(Player, playerNameText)

    won = False

    frameCount = 0
    while not won:
        if frameCount == 38:
            Player.pawn.switchPawn()
        frameCount += 1
        if frameCount > 60:
            Player.pawn.switchPawn()
            frameCount = 0

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

                    if i == NUMPLAYERS-1:
                        i = -1

                    i += 1
                    Player = playerList[i]

                if event.attr1 == 'ROLL':
                    roll(Player)

                if event.attr1 == 'COMPLETE':
                    time.sleep(.5)
                    for p in range(3):
                        if Player.deck.hand[p] == Player.location.name:
                            Player.deck.hand[p] = Player.deck.deck.pop()
                            if Player.deck.hand[p] == '':
                                Player.complete += 1
                            if Player.complete == 3: # if the player has no destinations left, give them northpole as destination.
                                Player.deck.hand[0] = "North Pole"
                            if Player.complete == 4 and Player.location.name == "North Pole":
                                pygame.event.post(WIN)

                if event.attr1 == 'WIN':
                    WinBox = pygame.Surface((800, 600))
                    background.blit(WinBox, (350, 100))
                    won = True

                if event.attr1 == 'RESET':
                    Player.goBack()

                if not won:
                    updateDesButtons(Player, buttonList)
                updateName(Player, playerNameText)
                updateRollView(Player, rollView)
                updateDestinationView(Player, handView)
                updateComplete(Player)

        pygame_widgets.update(events)
        pygame.display.update()

if __name__ == "__main__":
    main(6, 12)