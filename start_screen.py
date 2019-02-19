import pygame
import game_functions


class StartScreen:

    def __init__(self, settings, screen, stats, sb, ship, play_button, score_button,
                 aliens, bullets, alien_bullets, allien_type, barrier, ufo, explosion, number):
        self.screen = screen
        self.screen_color = (100, 100, 100)
        self.start_button = play_button
        self.high_score_button = score_button
        self.settings = settings
        self.stats = stats
        self.sb = sb
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets
        self.alien_type = allien_type
        self.barrier = barrier
        self.ufo = ufo
        self.alien_bullets = alien_bullets
        self.explosion = explosion
        self.number = number

        self.title_space = 'Space'
        self.title_invaders = 'Invaders'
        self.ten_p = '10 PTS'
        self.twenty_p = '20 PTS'
        self.forty_p = '40 PTS'
        self.screen_rect = screen.get_rect()
        self.GREEN = (0, 200, 0)
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 100)
        self.small_font = pygame.font.SysFont(None, 30)
        self.prep_title()

    def prep_title(self):
        self.title_space_image = self.font.render(self.title_space, True, self.WHITE)
        self.title_space_image_rect = self.title_space_image.get_rect()
        self.title_space_image_rect.top = self.screen_rect.top + 100
        self.title_space_image_rect.centerx = self.screen_rect.centerx

        self.title_invaders_image = self.font.render(self.title_invaders, True, self.GREEN)
        self.title_invaders_image_rect = self.title_invaders_image.get_rect()
        self.title_invaders_image_rect.top = self.screen_rect.top + 175
        self.title_invaders_image_rect.centerx = self.screen_rect.centerx

        for alien in range(1, 5):
            if alien == 1:
                self.alien_name = 'sprites/enemy1.png'
            elif alien == 2:
                self.alien_name = 'sprites/enemy2.png'
            elif alien == 3:
                self.alien_name = 'sprites/enemy3.png'
            elif alien == 4:
                self.alien_name = 'sprites/UFO.png'
            self.enemy = pygame.image.load(self.alien_name)
            self.enemy = pygame.transform.scale(self.enemy, (40, 50))
            self.enemy_rect = self.enemy.get_rect()
            self.enemy_rect.top = self.screen_rect.top + 200 + (75*alien)
            self.enemy_rect.centerx = self.screen_rect.centerx - 50
            self.screen.blit(self.enemy, self.enemy_rect)

            self.equal_sign = pygame.image.load('sprites/equal.png')
            # self.enemy = pygame.transform.scale(self.equal_sign, (4000, 5000))
            self.equal_sign_rect = self.equal_sign.get_rect()
            self.equal_sign_rect.top = self.screen_rect.top + 200 + (75 * alien)
            self.equal_sign_rect.centerx = self.screen_rect.centerx
            self.screen.blit(self.equal_sign, self.equal_sign_rect)

            if alien == 1:
                self.points = self.ten_p
            elif alien == 2:
                self.points = self.twenty_p
            elif alien == 3:
                self.points = self.forty_p
            elif alien == 4:
                self.points = '???'
            self.score = self.small_font.render(self.points, True, self.WHITE)
            self.score_rect = self.score.get_rect()
            self.score_rect.top = self.screen_rect.top + 200 + (75*alien)
            self.score_rect.centerx = self.screen_rect.centerx + 50
            self.screen.blit(self.score, self.score_rect)

    def draw_screen(self):
        self.screen.fill(self.screen_color)
        self.start_button.draw_button()
        self.high_score_button.draw_button()
        self.prep_title()
        self.screen.blit(self.title_space_image, self.title_space_image_rect)
        self.screen.blit(self.title_invaders_image, self.title_invaders_image_rect)
        self.screen.blit(self.enemy, self.enemy_rect)
        pygame.display.flip()

        game_functions.check_events(self.settings, self.screen, self.stats, self.sb, self.start_button,
                                    self.high_score_button, self.ship, self.aliens, self.bullets, self.alien_bullets,
                                    self.alien_type, self.barrier, self.ufo, self.explosion, self.number)
