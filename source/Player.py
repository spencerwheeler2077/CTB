from source import Pawn


class Player:
    def __init__(self, pawnimage, location, adjustments):
        self.adjustX = adjustments[0]
        self.adjustY = adjustments[1]
        self.pawn = Pawn.Pawn(pawnimage, location.adjustedLocation(self.adjustX, self.adjustY))
        self.location = location

    def goTo(self, newlocation):
        self.location = newlocation
        self.pawn.move(self.location.adjustedLocation(self.adjustX, self.adjustY))


