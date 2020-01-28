import os

import pygame
from pygame.sprite import Sprite


class Rocket():

    def __init__(self, game_settings, screen):
        """Initialize the rocket."""
        self.screen = screen
        self.game_settings = game_settings

        # Load image.
        self.image = pygame.image.load(os.path.join('images', 'rocket.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each rocket at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value of rocket center.
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

        # Movement flag.
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        """Update rocket's position based on the movement flag."""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.game_settings.rocket_speed_factor
        if self.move_left and self.rect.left > 0:
            self.centerx -= self.game_settings.rocket_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.game_settings.rocket_speed_factor
        if self.move_up and self.rect.top > 0:
            self.centery -= self.game_settings.rocket_speed_factor

        # Update rect object from self.centerx and self.centery
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw rocket on the screen."""
        self.screen.blit(self.image, self.rect)
