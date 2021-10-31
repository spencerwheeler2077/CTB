import random

import DestinationFactory

destinationList = DestinationFactory.destinationFactory()

class EventCard:
    def __init__(self, line):
        line = line.strip("]\n")
        items = line.split(", ")
        for i in range(len(items)):
            if items[i] == '':
                items[i] = 0
        self.text = items[0]

        self.location = destinationList[int(items[1])]
        self.nextTurn = int(items[2])
        self.bonus = int(items[3])
        self.give = bool(items[4])
        self.skip = bool(items[5])
        self.add = destinationList[int(items[6])].name



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


