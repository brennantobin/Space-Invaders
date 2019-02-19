# import sys
import pygame
import random
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from start_screen import StartScreen
# import logging
# from ufo import UFO


def run_game():

    # logger = logging.getLogger('tipper')
    # logger.addHandler(logging.StreamHandler())
    # logger.setLevel(logging.DEBUG)

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
    explosions = Group()
    alien_type = 'sprites/enemy3'
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    barriers = Group()
    ufos = Group()
    game_functions.create_fleet(settings, screen, ship, aliens, alien_type)
    sec = 3

    while True:

        if not stats.game_active:
            start_screen = StartScreen(settings, screen, stats, sb, ship, play_button, score_button,
                                       aliens, bullets, alien_bullets, alien_type, barriers, ufos, explosions)
            start_screen.draw_screen()

        game_functions.check_events(settings, screen, stats, sb, play_button, score_button, ship, aliens,
                                    bullets, alien_bullets, alien_type, barriers, ufos, explosions)

        if stats.game_active:
            ship.update()
            explosions.update()
            for explosion in explosions:
                if not explosion.is_exploding:
                    explosion.kill()
            for ufo in ufos:
                if (not ufo.moving) and random.randint(1, 100) == 2:
                    ufo.moving = True
                ufo.update()
            if len(ufos.sprites()) == 0:
                game_functions.create_ufo_group(settings, screen, ufos)

            game_functions.update_bullets(settings, screen, stats, sb, ship, aliens,
                                          bullets, alien_type, barriers, ufos, explosions)
            game_functions.update_alien_bullets(alien_bullets, barriers)
            game_functions.fire_alien_bullet(settings, screen, aliens, alien_bullets)
            now = pygame.time.get_ticks()
            wait = False
            if (now/1000) == sec:
                wait = True
                # logger.debug(now)
            if wait:
                game_functions.change_alien(aliens)
                sec += 1

            game_functions.update_aliens(settings, stats, screen, sb, ship, aliens, bullets, alien_type, explosions)
            game_functions.update_screen(settings, screen, stats, sb, ship, aliens, bullets, alien_bullets,
                                         play_button, barriers, ufos, explosions)
        game_functions.update_screen(settings, screen, stats, sb, ship, aliens, bullets,
                                     alien_bullets, play_button, barriers, ufos, explosions)


run_game()
