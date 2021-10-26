import DestinationFactory

class EventCard:
    def __init__(self, text, nextTurn=None, location=None, bonus=None, give=None, skip=None, add=None):
        self.text = text
        self.location = location
        self.nextTurn = nextTurn
        self.bonus = bonus
        self.give = give
        self.skip = skip
        self.add = add



class EventDeck:
    def __init__(self):
        self.destinationList = DestinationFactory.destinationFactory()
        self.deck = []
        self.file = open("resource/eventCardText")

        line = self.file.readline()
        self.deck.append(EventCard(line, location=self.destinationList[0]))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))

        line = self.file.readline()
        self.deck.append(EventCard(line))


        self.file.close()