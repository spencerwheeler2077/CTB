class Destination:

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.pointers = []

    def addPointers(self, *args):
        for i in args:
            self.pointers.append(i)

    def getLocation(self):
        return self.x, self.y

    def adjustedLocation(self, x, y):
        return self.x+x, self.y+y

    def getDirection(self, index):
        return self.pointers[index].destination, self.pointers[index].distance


