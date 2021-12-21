from pygame_widgets.button import Button


class CTBGButton(Button):
    def __init__(self, surface, leftPos, topPos, length, height, number=1, Dest=False):
        if Dest:
            font = 26
        else:
            font = 24
        super().__init__(surface, leftPos, topPos, length, height, fontSize=font)
        self.number = number


    def setString(self, newString):
        self.string = newString
        self.text = self.font.render(self.string, True, self.textColour)





