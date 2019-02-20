import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # the class represents a single alien in the fleet

    def __init__(self, settings, screen, alien_type, number):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        self.type = type
        self.alien_type = alien_type
        self.number = number
        self.image = pygame.image.load(alien_type + '.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        # draw the alien in it's location
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

