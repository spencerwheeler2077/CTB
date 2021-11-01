import random

import DestinationFactory

destinationList = DestinationFactory.destinationFactory()

class EventCard:
    def __init__(self, line):
        line = line.strip("]\n")
        items = line.split(", ")
        for i in range(len(items)):
            if items[i] == '':
                if i == 1 or i == 6:
                    items[i] = None
                else:
                    items[i] = 0

        self.wholeText = items[0]
        if len(self.wholeText) > 35:
            self.text1 = self.wholeText[0:34]
            self.text2 = self.wholeText[34:]
        else:
            self.text1 = self.wholeText
            self.text2 = ''

        if items[1] is not None:
            self.location = destinationList[int(items[1])]

        else:
            self.location = None
        self.nextTurn = int(items[2])
        self.bonus = int(items[3])
        self.give = bool(items[4])
        self.skip = bool(items[5])
        if items[6] is not None:
            self.add = destinationList[int(items[6])].name
        else:
            self.add= None
        self.extra = bool(items[7])

    def giveText(self):
        return [self.text1, self.text2]

#TODO add event card that switches player positions.


class EventDeck:
    def __init__(self):

        self.deck = []
        self.file = open("resource/eventCardText")
        self.file.readline()
        self.used = []
        for line in self.file:
            self.deck.append(EventCard(line))

        random.shuffle(self.deck)

        self.file.close()

    def giveEvent(self):
        top = self.deck.pop()
        self.used.append(top)
        if len(self.deck) == 0:
            self.deck = self.used
            self.used = []
            random.shuffle(self.deck)
        return top


