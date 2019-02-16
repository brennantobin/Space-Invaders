import sys
import pygame
#import threading
from bullet import Bullet
from alien import Alien
from time import sleep
from barrier import Barrier
from ufo import UFO
# from highscores import Highscores


def check_events(settings, screen, stats, sb, play_button, score_button, ship, aliens,
                 bullets, alien_type, barriers, ufo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets,
                              mouse_x, mouse_y, alien_type, barriers, ufo)
            check_score_button(settings, screen, stats, sb, score_button, mouse_x, mouse_y)


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button, barriers, ufo):
    screen.fill(settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #ufo.blitme()
    ufo.draw(screen)
    aliens.draw(screen)
    barriers.draw(screen)
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(settings, screen, stats, sb, ship, aliens, bullets, aliens_type, barriers, ufos):
    # update the bullet position
    bullets.update()
    # get rid of bullets after they leave the screen
    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets, aliens_type, barriers)
    check_bullet_ufo_collision(ufos, bullets)
    check_bullet_barrier_collisions(barriers, bullets)

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
    # for i in range(3):
        # new_bullet = Bullet(settings=settings, screen=screen, ship=ship, bullet_spacer=i * 0.5 * ship.rect.height)
        new_bullet = Bullet(settings=settings, screen=screen, ship=ship, bullet_spacer=0)
        bullets.add(new_bullet)


# def fire_alien_bullet(settings, screen, aliens, bullets):
#    if len(bullets) < settings.bullets_allowed:
#        new_bullet = Bullet(settings=settings, screen=screen, aliens=aliens, bullets=aliens.rect.height)
#        bullets.add(new_bullet)

def create_ufo_group(settings, screen, ufo):
    ufo_one = UFO(settings, screen)
    ufo.add(ufo_one)


def create_barriers(settings, screen, barriers):
    x_off = 80
    for column in range(0, 4):
        for piece in range(0, 6):
            create_barrier(settings, screen, barriers, piece, x_off)
        x_off += 300


def create_fleet(settings, screen, ship, aliens, alien_type):
    alien = Alien(settings, screen, alien_type)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            if row_number == 0:
                alien_type = 'sprites/enemy3'
            elif row_number < 2:
                alien_type = 'sprites/enemy2'
            elif row_number <= 3:
                alien_type = 'sprites/enemy1'

            create_alien(settings, screen, aliens, alien_number, row_number, alien_type)


def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(settings, screen, aliens, alien_number, row_number, alien_type):
    alien = Alien(settings, screen, alien_type)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number) + 50
    aliens.add(alien)


def create_barrier(settings, screen, barriers, piece, x_off):
    barrier = Barrier(settings, screen, piece, x_off)
    barriers.add(barrier)


def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def get_number_rows(settings, ship_height, alien_height):
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (3 * alien_height))
    return number_rows


def change_alien(aliens):
    #threading.Timer(1.0, change_alien, [aliens]).start()
    for alien in aliens:
        if alien.alien_type == alien.alien_type[0:14] + '(2)':
                alien.alien_type = alien.alien_type[0:14]
                alien.image = pygame.image.load(alien.alien_type + '.png')
        else:
                alien.alien_type = alien.alien_type[0:14] + '(2)'
                alien.image = pygame.image.load(alien.alien_type + '.png')


def update_aliens(settings, stats, screen, sb, ship, aliens, bullets, alien_type):
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, sb, ship, aliens, bullets, alien_type)
    check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets, alien_type)


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets, alien_type, barriers):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()

        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()

        create_fleet(settings, screen, ship, aliens, alien_type)
        create_barriers(settings, screen, barriers)


def check_bullet_barrier_collisions(barriers, bullets):
    pygame.sprite.groupcollide(bullets, barriers, True, True)


def check_bullet_ufo_collision(ufo, bullets):
    pygame.sprite.groupcollide(bullets, ufo, True, True)


def ship_hit(settings, stats, screen, sb, ship, aliens, bullets, alien_type):

    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens, alien_type)
        ship.center_ship()

        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets, alien_type):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, sb, ship, aliens, bullets, alien_type)
            break


def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x,
                      mouse_y, alien_type, barriers, ufo):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button, barriers, ufo)
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        barriers.empty()
        ufo.empty()

        create_fleet(settings, screen, ship, aliens, alien_type)
        create_barriers(settings, screen, barriers)
        create_ufo_group(settings, screen, ufo)
        ship.center_ship()


def check_score_button(settings, screen, stats, sb, score_button, mouse_x, mouse_y):
    button_clicked = score_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # display_scores = Highscores(settings, screen, stats, sb)
        # display_scores.make_screen()


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

