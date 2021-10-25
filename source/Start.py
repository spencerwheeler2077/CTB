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

    textBox = TextBox(win, sliderX, sliderY - 80, 650, outputHeight, fontSize=30)
    textBox.setText("Choose the number of Players, and number destinations desired")
    widgetList.append(textBox)

    playerSlider = Slider(win, sliderX, sliderY, sliderWidth, sliderHeight, min=2, max=6, step=1, initial=4)
    playerOutput = TextBox(win, sliderX + sliderWidth + 50, sliderY - 10, outputWidth, outputHeight, fontSize=25)
    playerOutput.disable()

    widgetList.append(playerSlider)
    widgetList.append(playerOutput)

    destinationSlider = Slider(win, sliderX, sliderY + sliderYDif, sliderWidth, sliderHeight,
                               min=10, max=26, step=1, initial=20)
    destinationOutput = TextBox(win, sliderX + sliderWidth + 50, sliderY + sliderYDif - 10, outputWidth, outputHeight,
                                fontSize=25)
    destinationOutput.disable()

    widgetList.append(destinationSlider)
    widgetList.append(destinationOutput)

    enter = Button(win, 400, 300, 150, 40, text="Enter", fontSize=30)
    enter.setOnClick(enterFun)
    widgetList.append(enter)



    run = True
    while run:
        events = pygame.event.get()

        win.fill((200, 225, 255))

        playerSlider.draw()
        destinationSlider.draw()

        playerOutput.setText(str(playerSlider.getValue()) + " Players")
        destinationOutput.setText(str(destinationSlider.getValue()) + " Destinations")

        playerOutput.draw()
        destinationOutput.draw()
        pygame_widgets.update(events)

        pygame.display.update()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.USEREVENT:
                numPlayers, deckSize = playerSlider.getValue(), destinationSlider.getValue()
                disableWidgets(widgetList)
                run = False
                main.main(numPlayers, deckSize)




if __name__ == "__main__":
    start()
