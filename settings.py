import os

import pygame


class Settings():
    """Settings for My Game."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.game_name = 'Meteorites Rush'
        self.background_image = os.path.join('images', 'space.jpg')

        # Settings rocket.
        self.rocket_speed_factor = 3
        self.rocket_lifes = 3

        # Bullet settings.
        self.bullet_speed_factor = 2
        self.bullets_allowed = 1
