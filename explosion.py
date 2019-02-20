import pygame
import random
from pygame.sprite import Sprite


class Explosion(Sprite):
    # the class represents a single alien in the fleet

    def __init__(self, settings, screen, position, explosion_type):
        super(Explosion, self).__init__()
        self.screen = screen
        self.settings = settings
        self.explosion_type = explosion_type
        self.is_exploding = True
        self.explosion_number = 0
        self.ufo_points = random.randint(40, 200)
        self.image = pygame.image.load('sprites/Explosion' + str(self.explosion_number) + '.png')
        self.rect = position

        self.go = True
        self.start_time = pygame.time.get_ticks()

    def blitme(self):
        # draw the alien in it's location
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.explosion_type == 'ship':
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

        if self.explosion_type == 'ufo':
            time = pygame.time.get_ticks()
            time_variant = 700
            WHITE = (255, 255, 255)
            font = pygame.font.SysFont(None, 50)
            self.image = font.render(str(self.ufo_points), True, WHITE)
            if time > (time_variant + self.start_time):
                self.is_exploding = False

        if self.explosion_type == 'alien':
            time_variant = 10 * self.explosion_number
            if self.go:
                self.image = pygame.image.load('sprites/Explosion' + str(self.explosion_number) + '.png')
            time = pygame.time.get_ticks()
            if time > (time_variant + self.start_time):
                self.go = True
            else:
                self.go = False
            self.explosion_number += 1
            if self.explosion_number > 4:
                self.explosion_number = 0
                self.is_exploding = False
