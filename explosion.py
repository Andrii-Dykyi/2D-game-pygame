import os

import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """Represent explosion."""

    def __init__(self, screen, rocket):
        """Create an explosion object at the rocket's current position."""
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load(os.path.join('images', 'explo.png'))
        self.rect = self.image.get_rect()

        self.rect.centerx = rocket.rect.centerx
        self.rect.centery = rocket.rect.top
        self.y = self.rect.y

    def update(self):
        """Move the explosion down the screen."""
        self.y += 3
        # Update the rect position.
        self.rect.y = self.y

    def blit_explosion(self):
        """Draw the explosion to the screen."""
        self.screen.blit(self.image, self.rect)
