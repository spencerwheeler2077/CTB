

class DestinationDeck():
    def __init__(self):
        filepath = 'resource/Destinations'
        self.deck = []
        file = open(filepath)
        for line in file:
            self.deck.append(line.strip('\n'))

    def pop(self):
        return self.deck.pop()

class Hand():
    def __init__(self):
        self.hand = []
        self.deck = DestinationDeck()
        for i in range(3):
            self.hand.append(self.deck.pop())

    def addToHand(self):
        if len(self.hand)<3:
            self.hand.append(self.deck.pop())

