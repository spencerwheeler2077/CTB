import random


class DestinationDeck:
    def __init__(self, deckSize):
        filepath = 'resource/Destinations'
        self.deck = []
        file = open(filepath)
        for line in file:
            self.deck.append(line.strip('\n'))
        random.shuffle(self.deck)
        self.deck = self.deck[:deckSize]
        random.shuffle(self.deck)

    def pop(self):
        if len(self.deck) == 0:
            return ''
        return self.deck.pop()

    def add(self, destination):
        self.deck.append(destination)

    def giveLength(self):
        return len(self.deck)


class Hand:
    def __init__(self, deckSize):
        self.hand = []
        self.deck = DestinationDeck(deckSize)
        for i in range(3):
            self.hand.append(self.deck.pop())

    def addToHand(self):
        if len(self.hand) < 3:
            self.hand.append(self.deck.pop())

    def giveDeckLen(self):
        return self.deck.giveLength()


