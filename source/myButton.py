from pygame_widgets.button import Button

class CTBGButton(Button):
    def __init__(self, surface, leftPos, topPos, length, height, number=1):
        super().__init__(surface, leftPos, topPos, length, height)
        self.number = number


    def setString(self, newString):
        self.string = newString
        self.text = self.font.render(self.string, True, self.textColour)





