import pygame.font


class Scoreboard():
    """A class to respond scoring info."""

    def __init__(self, game_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # Font settings for scoring info.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_life()

    def prep_score(self):
        """Turn the score into a rendered image."""
        self.score_image = self.font.render(f'Score: {self.stats.score}',
                                            True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_life(self):
        """Turn the level into a rendered image."""
        self.life_image = self.font.render(
                f'Lifes left: {self.stats.rocket_life}', True, self.text_color)

        # Position.
        self.life_rect = self.life_image.get_rect()
        self.life_rect.left = self.screen_rect.left + 20
        self.life_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.life_image, self.life_rect)
