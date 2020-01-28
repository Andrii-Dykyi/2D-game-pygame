import os
import random

import pygame
from pygame.sprite import Sprite


class Meteorite(Sprite):
    """Represent a single meteorite."""

    def __init__(self, game_settings, screen):
        """Initialize the meteorite and its starting position."""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load the image of meteorite and its rect attribute.
        self.image = pygame.image.load(os.path.join('images',
                                                    'meteorite.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new meteorite.
        self.rect.x = random.randint(0, 1200 - 50)
        self.rect.y = self.screen_rect.top - 74
        self.y = self.rect.y

    def update(self):
        """Move the bullet up the screen."""
        self.y += 3
        # Update the rect position.
        self.rect.y = self.y

    def blit_meteorite(self):
        """Draw the meteorite on its current position."""
        self.screen.blit(self.image, self.rect)
