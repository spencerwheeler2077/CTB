class Pointer:

    def __init__(self, destination, distance):
        self.__destination = destination
        self.__distance = distance

    def giveDestination(self):
        return self.__destination

    def giveDistance(self):
        return self.__distance
