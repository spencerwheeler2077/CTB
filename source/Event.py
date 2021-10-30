import DestinationFactory

destinationList = DestinationFactory.destinationFactory()

class EventCard:
    def __init__(self, line):
        items = line.split(", ")
        for i in range(len(items)):
            if items[i] == '':
                items[i] = None
        self.text = line[0]
        self.location = destinationList[int(line[1])]
        self.nextTurn = line[2]
        self.bonus = line[3]
        self.give = line[4]
        self.skip = line[5]
        self.add = destinationList[int(line[6])]



class EventDeck:
    def __init__(self):

        self.deck = []
        self.file = open("resource/eventCardText")
        self.file.readline()
        for line in self.file:
            self.deck.append(EventCard(line))

        self.file.close()
