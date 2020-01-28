import os

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets fired from rocket."""

    def __init__(self, game_settings, screen, rocket):
        """Create a bullet object at the rocket's current position."""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load(os.path.join('images', 'bullet.png'))
        self.rect = self.image.get_rect()

        self.rect.centerx = rocket.rect.centerx
        self.rect.centery = rocket.rect.centery
        self.rect.top = rocket.rect.top

        self.y = self.rect.y

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.game_settings.bullet_speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def blit_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
