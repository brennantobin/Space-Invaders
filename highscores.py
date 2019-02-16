import pygame
#import game_functions
from button import Button
import game_functions


class Highscores:

    def __init__(self, settings, screen, stats, sb, ship, play_button, score_button, aliens, bullets, allien_type):

        self.start_button = play_button
        self.high_score_button = score_button
        self.stats = stats
        self.sb = sb
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets
        self.alien_type = allien_type

        self.screen = screen
        self.screen_color = (100, 100, 100)
        self.back_button = Button(screen, "back", 300)
        self.settings = settings
        self.stats = stats
        self.sb = sb
        self.title_space = 'High'
        self.title_invaders = 'Scores'
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 100)
        self.small_font = pygame.font.SysFont(None, 30)

    def make_screen(self):
        self.screen.fill(self.screen_color)
        self.sb.show_score()
        self.back_button.draw_button()

        pygame.display.flip()

        game_functions.check_events(self.settings, self.screen, self.stats, self.sb, self.back_button,
                                    self.high_score_button, self.ship, self.aliens, self.bullets, self.alien_type)
