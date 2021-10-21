from source import Pawn
import Hand
import random


class Player:
    def __init__(self, name, pawnimage, location, adjustments):
        self.adjustX = adjustments[0]
        self.adjustY = adjustments[1]
        self.pawn = Pawn.Pawn(pawnimage, location.adjustedLocation(self.adjustX, self.adjustY))
        self.location = location
        self.deck = Hand.Hand()
        self.name = name
        self.rollCount = 0
        self.hasRolled = False
        self.previousLocation = location
        self.preRollCount = 0
        self.complete = 0

    def goTo(self, info):

        self.previousLocation = self.location
        newLocation = info[0]
        distance = info[1]
        self.preRollCount = self.rollCount
        self.rollCount -= distance
        self.location = newLocation
        self.pawn.move(self.location.adjustedLocation(self.adjustX, self.adjustY))

    def roll(self):
        if not self.hasRolled:
            self.rollCount = random.randint(1, 6)
            self.hasRolled = True
        else:
            return self.rollCount

    def reset(self):
        self.hasRolled = False
        self.rollCount = 100
        self.previousLocation = self.location
        self.preRollCount = 0

    def goBack(self):
        self.location = self.previousLocation
        self.rollCount = self.preRollCount
        self.pawn.move(self.location.adjustedLocation(self.adjustX, self.adjustY))



