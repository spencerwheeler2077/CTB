import Pawn

class Player:
    def __init__(self, pawnimage, location):
        self.pawn = Pawn.Pawn(pawnimage, location.getLocation())
        self.location = location



