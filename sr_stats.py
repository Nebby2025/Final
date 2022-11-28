class GameStats:
    """Track stats for SRNW"""

    def __init__(self, sr_game):
        """Initialize stats"""
        self.settings = sr_game.settings
        self.reset_stats()
        self.high_score = 0
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that change during the game"""
        self.score = 0

    def maintained_stats(self):
        """Initialize stats that do not change"""
        self.high_score += self.score