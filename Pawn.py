import pygame

class Pawn(pygame.sprite.Sprite):
    def __init__(self, imagepath, location):
        pygame.sprite.Sprite.__init__(self),
        self.image = pygame.image.load(imagepath)
        self.rect = self.image.get_rect()
        self.rect.center = location

class Grid(pygame.sprite.Sprite):
    def __init__(self, imagepath):
        pygame.sprite.Sprite.__init__(self),
        self.image = pygame.image.load(imagepath)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

