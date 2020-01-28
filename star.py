import random
import os

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Repsent a single star."""

    def __init__(self, game_settings, screen):
        """Initialize a star and its position."""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load the image of star and its rect attribute.
        self.image = pygame.image.load(os.path.join('images', 'star.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new meteorite.
        self.rect.x = random.randint(0, 1200 - 50)
        self.rect.y = self.screen_rect.top - 74
        self.y = self.rect.y
        self.x = self.rect.x

    def update(self):
        """Move the bullet up the screen."""
        self.y += 1

        # Update the rect position.
        self.rect.y = self.y
        self.rect.x = self.x

    def blit_star(self):
        """Draw the meteorite on its current position."""
        self.screen.blit(self.image, self.rect)
