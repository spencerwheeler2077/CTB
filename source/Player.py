from source import Pawn
import Hand
import random


class Player:
    def __init__(self, name, pawnimage, location, adjustments, deckSize):
        self.adjustX = adjustments[0]
        self.adjustY = adjustments[1]
        self.pawn = Pawn.Pawn(pawnimage, location.adjustedLocation(self.adjustX, self.adjustY))
        self.location = location
        self.deck = Hand.Hand(deckSize)
        self.name = name
        self.rollCount = 0
        self.hasRolled = False
        self.previousLocation = location
        self.preRollCount = 0
        self.complete = 0
        self.nextTurn = 0
        self.bonus = 0

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
            self.rollCount = self.rollCount + random.randint(1, 6)
            self.hasRolled = True
        else:
            return self.rollCount

    def useBonus(self):
        if self.bonus <= 0:
            return
        else:
            self.rollCount = self.rollCount + 1
            self.bonus = self.bonus - 1


    def reset(self):
        self.pawn.reset()
        self.hasRolled = False
        self.rollCount = self.nextTurn
        self.nextTurn = 0
        self.previousLocation = self.location
        self.preRollCount = 0

    def goBack(self):
        self.location = self.previousLocation
        self.rollCount = self.preRollCount
        self.pawn.move(self.location.adjustedLocation(self.adjustX, self.adjustY))

    def useEvent(self, event):

        if event.location is not None:
            self.location = event.location
            self.pawn.move(self.location.adjustedLocation(self.adjustX, self.adjustY))

        if event.nextTurn != 0:
            self.nextTurn = event.nextTurn

        if event.bonus != 0:
            self.bonus += event.bonus

        if event.give:
            if self.deck.giveDeckLen() > 0:
                return self.deck.deck.pop()

        if event.skip:
            self.deck.deck.pop()

        if event.add is not None:
            self.deck.deck.add(event.add)

        if event.extra:
            return 'extra'

        return None

