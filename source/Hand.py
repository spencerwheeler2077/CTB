import random


class DestinationDeck:
    def __init__(self, deckSize):
        filepath = 'resource/Destinations'
        self.deck = []
        file = open(filepath)
        for line in file:
            self.deck.append(line.strip('\n'))
        random.shuffle(self.deck)
        self.deck = self.deck[:(deckSize-1)]  # minus one because because 0 is included.
        random.shuffle(self.deck)

    def pop(self):
        if len(self.deck) == 0:
            return ''
        return self.deck.pop()


class Hand:
    def __init__(self, deckSize):
        self.hand = []
        self.deck = DestinationDeck(deckSize)
        for i in range(3):
            self.hand.append(self.deck.pop())

    def addToHand(self):
        if len(self.hand) < 3:
            self.hand.append(self.deck.pop())

