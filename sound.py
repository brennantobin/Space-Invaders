import pygame


class Sound:

    def __init__(self):
        self.second1 = 2
        self.second2 = 3
        self.second3 = 4
        self.second4 = 5
        self.ufo_sec = 0
        self.vary1 = 0
        self.vary2 = 0
        self.vary3 = 0
        self.vary4 = 0
        self.faster_vary = 0
        self.even_faster_vary = 0
        self.faster = False
        self.even_faster = False
        self.faster_stop = False
        self.even_faster_stop = False

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
        if self.faster and not self.faster_stop:
            self.vary1 += 0.5
            self.vary3 -= 0.5
            self.vary4 -= 1
            self.faster_stop = True
            self.faster_vary = 2
        if self.even_faster and self.even_faster_stop:
            self.vary1 += 0.25
            self.vary2 -= 0.5
            self.vary3 -= 1.25
            self.vary4 -= 2
            self.even_faster_stop = True
            self.even_faster_vary = 3
        # makes it so each beep in the background music is playing once a second
        # Increase the spead of the music as the aliens die
        if round(start_time/1000.00*4)/4 == self.second1 + self.vary1:
            hold1 = True
        if hold1:
            fastinvader1.play()
            self.second1 += (4.00 - self.faster_vary - self.even_faster_vary)
        if round(start_time/1000.00*4)/4 == self.second2 + self.vary2:
            hold2 = True
        if hold2:
            fastinvader2.play()
            self.second2 += (4.00 - self.faster_vary - self.even_faster_vary)
        if round(start_time/1000.00*4)/4 == self.second3 + self.vary3:
            hold3 = True
        if hold3:
            fastinvader3.play()
            self.second3 += (4.00 - self.faster_vary - self.even_faster_vary)
        if round(start_time/1000.00*4)/4 == self.second4 + self.vary4:
            hold4 = True
        if hold4:
            fastinvader4.play()
            self.second4 += (4.00 - self.faster_vary - self.even_faster_vary)
