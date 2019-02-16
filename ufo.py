import pygame
from pygame.sprite import Sprite


class UFO(Sprite):

    def __init__(self, settings, screen):
        super(UFO, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('sprites/UFO.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.left - 60
        self.rect.top = self.screen_rect.top + 60

        self.center = float(self.rect.centerx)
        self.moving = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # shouldn't do anything unless the ufo is supposed to be moving
        if self.moving:
            # check direction and make sure it hasn't reached the end
            if self.moving_right and self.center < (self.screen_rect.right + 50):
                self.center += self.settings.ufo_speed

            elif self.moving_left and self.center > self.screen_rect.left - 50:
                self.center -= self.settings.ufo_speed

            # when it reaches the end change its direction and stop it from moving
            elif self.moving_right:
                self.moving_right = False
                self.moving_left = True
                self.moving = False

            else:
                self.moving_left = False
                self.moving_right = True
                self.moving = False
            self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
