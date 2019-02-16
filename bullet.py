import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # class to hold all things related to bullets

    # def __init__(self, settings, screen, ship):
    def __init__(self, settings, screen, ship, bullet_spacer=0):

        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - bullet_spacer

        self.y = float(self.rect.y - bullet_spacer)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        # moving the bullet

        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # draw the bullet onto the screen
        pygame.draw.rect(self.screen, self.color, self.rect)