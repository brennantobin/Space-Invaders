# import sys
import pygame
import threading
import random
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from start_screen import StartScreen
# from ufo import UFO


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    play_button = Button(screen, "play", 200)
    score_button = Button(screen, 'high scores', 300)
    # back_button = Button(screen, "back", 300)
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(settings, screen, stats)
    # ufo = UFO(settings, screen, stats)
    alien_type = 'sprites/enemy3'
    bullets = Group()
    aliens = Group()
    barriers = Group()
    ufos = Group()
    game_functions.create_fleet(settings, screen, ship, aliens, alien_type)

    while True:

        if not stats.game_active:
            start_screen = StartScreen(settings, screen, stats, sb, ship, play_button, score_button,
                                       aliens, bullets, alien_type, barriers, ufos)
            start_screen.draw_screen()

        game_functions.check_events(settings, screen, stats, sb, play_button, score_button, ship, aliens,
                                    bullets, alien_type, barriers, ufos)

        if stats.game_active:
            ship.update()
            for ufo in ufos:
                if (not ufo.moving) and random.randint(1, 100) == 2:
                    ufo.moving = True
                ufo.update()
            game_functions.update_bullets(settings, screen, stats, sb, ship, aliens, bullets, alien_type, barriers, ufos)
            # game_functions.change_alien(aliens)
            timer = threading.Timer(1.0, game_functions.change_alien, [aliens])
            timer.start()
            game_functions.update_aliens(settings, stats, screen, sb, ship, aliens, bullets, alien_type)
            game_functions.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button, barriers, ufos)
            timer.cancel()

        game_functions.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button, barriers, ufos)


run_game()
