import pygame
from pygame.sprite import Sprite


class Barrier(Sprite):
    # the class represents a single barrier in the group

    def __init__(self, settings, screen, piece, x_off):
        super(Barrier, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('sprites/BarrierPiece' + str(piece) + '.png')
        # self.image = pygame.transform.scale(self.image, (1000, 900))
        self.rect = self.image.get_rect()

        self.rect.x = x_off
        self.rect.top = 600 

    def blitme(self):
        # draw the barrier in it's location
        self.screen.blit(self.image, self.rect)
