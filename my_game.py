import pygame
from pygame.sprite import Group

import game_functions
from button import Button
from game_stats import GameStats
from descript_game import Description
from meteorite import Meteorite
from rocket import Rocket
from score import Scoreboard
from settings import Settings


def run_game():
    """Initialize a game, display."""
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.game_name)

    # Make the Play button.
    play_button = Button(game_settings, screen, "Play")
    # Make describtion.
    description = Description(game_settings, screen, "Project by Andrii Dykyi")
    # Create an instance to store game statistics.
    stats = GameStats(game_settings)
    score_board = Scoreboard(game_settings, screen, stats)

    background_image = pygame.image.load(
        game_settings.background_image).convert()

    # Create rocket.
    rocket = Rocket(game_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()
    # Make a meteorite.
    meteorites = Group()
    # Make a star.
    stars = Group()
    # Make an explosion.
    explosions = Group()

    while True:
        game_functions.check_event(game_settings, screen, stats,
                                   play_button, rocket, meteorites,
                                   stars, bullets, score_board, explosions)

        if stats.game_active:
            rocket.update()

            game_functions.update_bullets(bullets, screen, meteorites)

            game_functions.update_meteorites(game_settings, stats, screen,
                                             rocket, meteorites, score_board,
                                             explosions)

            game_functions.update_explosions(explosions)

            game_functions.update_stars(game_settings, stats, screen,
                                        rocket, stars, score_board)

        game_functions.update_screen(background_image, game_settings, screen,
                                     stats, score_board, rocket, stars,
                                     meteorites, bullets, play_button,
                                     explosions, description)


if __name__ == '__main__':
    run_game()
