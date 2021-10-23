class EventCard:
    def __init__(self, text, nextTurn, location=None, bonus=None, give=None, skip=None, add=None):
        self.text = text
        self.location = location
        self.nextTurn = nextTurn
        self.bonus = bonus
        self.give = give
        self.skip = skip
        self.add = add


class EventDeck:
    def __init__(self):
        deck = []
        deck.append(EventCard("North Pole", None))