import pygame


class Pawn(pygame.sprite.Sprite):

    def __init__(self, imagepath, location):
        pygame.sprite.Sprite.__init__(self),
        self.image = pygame.image.load(imagepath)
        self.ogImage = self.image
        self.altImage = pygame.image.load("resource/greypawn.png")
        self.ogAltImage = self.altImage
        self.rect = self.image.get_rect()
        self.rect.center = location

    def move(self, location):
        self.rect.center = location

    def switchPawn(self):
        oldImage = self.image
        self.image = self.altImage
        self.altImage = oldImage

    def reset(self): # resets the images to what they are originally
        self.image = self.ogImage
        self.altImage = self.ogAltImage


class Grid(pygame.sprite.Sprite):

    def __init__(self, imagepath):
        pygame.sprite.Sprite.__init__(self),
        self.image = pygame.image.load(imagepath)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

