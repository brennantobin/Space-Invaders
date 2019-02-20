import pygame


class Sound:

    def __init__(self):
        self.second1 = 2
        self.second2 = 3
        self.second3 = 4
        self.second4 = 5

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
        if (start_time / 1000) == self.second1:
            hold1 = True
        if hold1:
            print (str(start_time) + ' , hold1')
            fastinvader1.play()
            self.second1 += 4
        if (start_time / 1000) == self.second2:
            hold2 = True
        if hold2:
            print (str(start_time) + ' , hold2')
            fastinvader2.play()
            self.second2 += 4
        if (start_time / 1000) == self.second3:
            hold3 = True
        if hold3:
            print (str(start_time) + ' , hold3')
            fastinvader3.play()
            self.second3 += 4
        if (start_time / 1000) == self.second4:
            hold4 = True
        if hold4:
            print (str(start_time) + ' , hold4')
            fastinvader4.play()
            self.second4 += 4
