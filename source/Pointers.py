class Pointer:

    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance
        self.name = self.destination.name

    def giveName(self):

        return self.name

    def giveDistance(self):
        return self.distance
