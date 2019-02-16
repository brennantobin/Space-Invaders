import pygame
from pygame.sprite import Sprite
# from scoreboard import Scoreboard


class Ship(Sprite):

    def __init__(self, settings, screen, stats):
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats

        self.image = pygame.image.load('sprites/ship.png')
        # self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

  #  def explode_ship(self):
