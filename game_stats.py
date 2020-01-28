class GameStats():
    """Track statistics."""

    def __init__(self, game_settings):
        """Initialize statistics."""
        self.game_settings = game_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rocket_life = self.game_settings.rocket_lifes
        self.score = 0
        self.level = 1
