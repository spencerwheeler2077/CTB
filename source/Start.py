import main
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button


def disableWidgets(list):

    for i in list:
        i.disable()
        i.hide()

def enterFun():
    pygame.event.post(pygame.event.Event(pygame.USEREVENT))


def start():
    widgetList = []
    pygame.init()
    win = pygame.display.set_mode((1500, 830))
    pygame.display.set_caption("Start menu")
    sliderX = 20
    sliderY = 100
    sliderWidth = 400
    sliderHeight = 20
    outputWidth = 150
    outputHeight = 50

    sliderYDif = 100

    textBox = TextBox(win, sliderX, sliderY - 15, 650, outputHeight, fontSize=30)
    textBox.setText("Choose number destinations each player needs to complete")
    widgetList.append(textBox)


    playerIntro = TextBox(win, 50, 290, 950, outputHeight, fontSize=45)
    playerIntro.setText("Enter your name in a box, its outline determines your piece color")
    playerIntro.disable()

    widgetList.append(playerIntro)

    destinationSlider = Slider(win, sliderX, sliderY + sliderYDif, sliderWidth, sliderHeight,
                               min=10, max=26, step=1, initial=15)
    destinationOutput = TextBox(win, sliderX + sliderWidth + 50, sliderY + sliderYDif - 10, outputWidth, outputHeight,
                                fontSize=25)
    destinationOutput.disable()

    nameWidth = 200
    nameHeight = 60

    playername1 = TextBox(win, 100, 350, nameWidth, nameHeight, fontSize=45)
    playername1.borderColour = (255, 255, 0)
    playername2 = TextBox(win, 350, 350, nameWidth, nameHeight, fontSize=45)
    playername2.borderColour = (0, 20, 255)
    playername3 = TextBox(win, 100, 450, nameWidth, nameHeight, fontSize=45)
    playername3.borderColour = (0, 180, 0)
    playername4 = TextBox(win, 350, 450, nameWidth, nameHeight, fontSize=45)
    playername4.borderColour = (255, 255, 255)
    playername5 = TextBox(win, 100, 550, nameWidth, nameHeight, fontSize=45)
    playername5.borderColour = (255, 180, 0)
    playername6 = TextBox(win, 350, 550, nameWidth, nameHeight, fontSize=45)
    playername6.borderColour = (230, 0, 0)
    playername1.draw()
    playername2.draw()
    playername3.draw()
    playername4.draw()
    playername5.draw()
    playername6.draw()



    widgetList.append(playername1)
    widgetList.append(playername2)
    widgetList.append(playername3)
    widgetList.append(playername4)
    widgetList.append(playername5)
    widgetList.append(playername6)

    widgetList.append(destinationSlider)
    widgetList.append(destinationOutput)

    enter = Button(win, 1000, 700, 300, 60, text="START GAME", fontSize=50)
    enter.setOnClick(enterFun)
    widgetList.append(enter)



    run = True
    while run:
        events = pygame.event.get()

        win.fill((200, 225, 255))

        destinationSlider.draw()

        destinationOutput.setText(str(destinationSlider.getValue()) + " Destinations")



        playerIntro.draw()
        destinationOutput.draw()
        pygame_widgets.update(events)

        pygame.display.update()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.USEREVENT:
                deckSize = destinationSlider.getValue()
                nameList = [playername1.getText(), playername2.getText(), playername3.getText(),
                            playername4.getText(), playername5.getText(), playername6.getText()]
                count = 0
                for name in nameList:
                    if name != "":
                        count = count+1
                if count < 2:
                    break

                disableWidgets(widgetList)
                run = False
                main.main(nameList, deckSize)




if __name__ == "__main__":
    start()
