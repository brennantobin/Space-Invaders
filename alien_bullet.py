import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    # class to hold all things related to bullets

    # def __init__(self, settings, screen, ship):
    def __init__(self, settings, screen, alien):

        super(AlienBullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        # moving the bullet

        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # draw the bullet onto the screen
        pygame.draw.rect(self.screen, self.color, self.rect)