import pygame


class Sound:

    def __init__(self):
        self.second1 = 2
        self.second2 = 3
        self.second3 = 4
        self.second4 = 5
        self.ufo_sec = 0
        self.faster = False
        self.even_faster = False

    def shoot(self):
        shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
        shoot_sound.play()

    def ship_hit(self):
        hit_sound = pygame.mixer.Sound('sounds/explosion.wav')
        hit_sound.play()

    def alien_hit(self):
        hit_sound = pygame.mixer.Sound('sounds/invaderkilled.wav')
        hit_sound.play()

    def background_music(self):
        start_time = pygame.time.get_ticks()
        fastinvader1 = pygame.mixer.Sound('sounds/fastinvader1.wav')
        fastinvader2 = pygame.mixer.Sound('sounds/fastinvader2.wav')
        fastinvader3 = pygame.mixer.Sound('sounds/fastinvader3.wav')
        fastinvader4 = pygame.mixer.Sound('sounds/fastinvader4.wav')
        hold1 = False
        hold2 = False
        hold3 = False
        hold4 = False
        if round((start_time / 1000), 1) == self.second1:
            hold1 = True
        if hold1:
            fastinvader1.play()
            self.second1 += 4
        if round((start_time / 1000), 1) == self.second2:
            hold2 = True
        if hold2:
            fastinvader2.play()
            self.second2 += 4
        if round((start_time / 1000), 1) == self.second3:
            hold3 = True
        if hold3:
            fastinvader3.play()
            self.second3 += 4
        if round((start_time / 1000), 1) == self.second4:
            hold4 = True
        if hold4:
            fastinvader4.play()
            self.second4 += 4
