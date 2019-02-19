import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    # the class represents a single alien in the fleet

    def __init__(self, settings, screen, position):
        super(Explosion, self).__init__()
        self.screen = screen
        self.settings = settings
        self.is_exploding = True
        self.explosion_number = 0
        self.image = pygame.image.load('sprites/Explosion' + str(self.explosion_number) + '.png')
       # self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = position

        self.go = True
        self.start_time = pygame.time.get_ticks()

    def blitme(self):
        # draw the alien in it's location
        self.screen.blit(self.image, self.rect)

    def update(self, explosions):
        time_variant = 10 * self.explosion_number
        if self.go:
            self.image = pygame.image.load('sprites/Explosion' + str(self.explosion_number) + '.png')
        time = pygame.time.get_ticks()
        if time > (time_variant + self.start_time):
            self.go = True
        else:
            self.go = False
        self.explosion_number += 1
        if self.explosion_number > 11:
            self.explosion_number = 0
            self.is_exploding = False

