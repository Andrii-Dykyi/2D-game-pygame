import sys

import pygame
from bullet import Bullet
from explosion import Explosion
from meteorite import Meteorite
from rocket import Rocket
from star import Star


def check_keydown_events(event, game_settings, screen, rocket, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        rocket.move_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        rocket.move_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        rocket.move_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        rocket.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(game_settings, screen, rocket, bullets)


def fire_bullets(game_settings, screen, rocket, bullets):
    """Fire a bullet if limit not reached."""
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, rocket)
        bullets.add(new_bullet)


def check_keyup_events(event, rocket):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        rocket.move_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        rocket.move_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        rocket.move_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        rocket.move_down = False


def check_event(
        game_settings, screen, stats, play_button,
        rocket, meteorites, stars, bullets,
        score_board, explosions):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats,
                              play_button, rocket, meteorites,
                              stars, bullets, mouse_x,
                              mouse_y, score_board, explosions)


def check_play_button(
        game_settings, screen, stats, play_button,
        rocket, meteorites, stars, bullets, mouse_x,
        mouse_y, score_board, explosions):
    """Starts a game."""
    if (play_button.rect.collidepoint(mouse_x, mouse_y)
            and not stats.game_active):
        stats.reset_stats()
        stats.game_active = True

        # Empty the lists of sprites.
        meteorites.empty()
        bullets.empty()
        stars.empty()
        explosions.empty()

        # Update life and score values.
        score_board.prep_life()
        score_board.prep_score()


def create_star(game_settings, screen, stars):
    """Create a star."""
    star = Star(game_settings, screen)
    stars.add(star)


def create_row_stars(game_settings, stats, screen, rocket, stars):
    """Create row of stars."""
    star = Star(game_settings, screen)
    number_stars = 1

    for star_number in range(number_stars):
        create_star(game_settings, screen, stars)


def update_stars(game_settings, stats, screen, rocket, stars, score_board):
    """Draw, move abd remove stars."""
    stars.update()

    # Create one star.
    if len(stars) < 1:
        create_row_stars(game_settings, stats, screen, rocket, stars)

    # Delete star which have dissapeared..
    for star in stars.copy():
        if star.rect.top >= star.screen_rect.bottom:
            stars.remove(star)

    # Add 1 point to score and delete when rocket collides a star.
    if pygame.sprite.spritecollideany(rocket, stars):
        stats.score += 1
        score_board.prep_score()
    pygame.sprite.spritecollide(rocket, stars, True)


def ship_hit(game_settings, stats, screen, rocket, meteorites, score_board):
    """Respond to ship being hit by alien."""
    # Decrement rocket's life.
    if stats.rocket_life > 0:
        stats.rocket_life -= 1
        score_board.prep_life()

    # When life < 0 stops the game.
    else:
        stats.game_active = False


def create_meteorite(game_settings, screen, meteorites, meteorite_number):
    """Create a meteorite and put it in the row."""
    meteorite = Meteorite(game_settings, screen)
    meteorites.add(meteorite)


def create_row_meteorites(game_settings, stats, screen, rocket, meteorites):
    """Create row of meteorites."""
    number_meteorites = 1

    for meteorite_number in range(number_meteorites):
        create_meteorite(game_settings, screen, meteorites, meteorite_number)


def update_explosions(explosions):
    """Update position of bullets and get rid of bullets
    that have disappeared."""
    # Update position of bullets.
    explosions.update()

    # Get rid of bullets that have disappeared.
    for explosion in explosions.copy():
        if explosion.rect.bottom <= 0:
            explosions.remove(explosion)


def update_meteorites(
        game_settings, stats, screen, rocket,
        meteorites, score_board, explosions):
    """Draw, move and remove meteorites."""
    meteorites.update()

    # Delete meteorites
    for meteorite in meteorites.copy():
        if meteorite.rect.top >= meteorite.screen_rect.bottom:
            meteorites.remove(meteorite)

    # Create roe of meteorites.
    if len(meteorites) < 10:
        create_row_meteorites(game_settings, stats, screen, rocket, meteorites)

    for meteorite in meteorites:
        if meteorite.rect.top == meteorite.screen_rect.centery - 300:
            create_row_meteorites(game_settings, stats,
                                  screen, rocket, meteorites)

    # Create explosion when rocket collides meteorite.
    if pygame.sprite.spritecollideany(rocket, meteorites):
        ship_hit(game_settings, stats, screen, rocket, meteorites, score_board)
        explosion = Explosion(screen, rocket)
        explosions.add(explosion)
        update_explosions(explosions)

    # Delete meteorite which hit the rocket.
    pygame.sprite.spritecollide(rocket, meteorites, True)


def update_bullets(bullets, screen, meteorites):
    """Update position of bullets and get rid of bullets
    that have disappeared."""
    # Update position of bullets.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Delete the bullet and the meteorite which hit each other.
    pygame.sprite.groupcollide(bullets, meteorites, True, True)


def update_screen(
        background_image, game_settings, screen, stats,
        score_board, rocket, stars, meteorites,
        bullets, play_button, explosions, description):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass throught the loop.
    screen.blit(background_image, (0, 0))

    # Redraw all bullets behind rocket.
    for bullet in bullets.sprites():
        bullet.blit_bullet()

    # Redraw rocket.
    rocket.blitme()

    # Redraw meteorites.
    meteorites.draw(screen)

    # Redraw all explosions.
    for explosion in explosions.sprites():
        explosion.blit_explosion()

    # Redraw stars.
    stars.draw(screen)

    # Draw the score info.
    score_board.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
        description.draw_description()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
