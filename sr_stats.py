class GameStats:
    """Track stats for SRNW"""

    def __init__(self, sr_game):
        """Initialize stats"""
        self.settings = sr_game.settings
        self.reset_stats()
        with open('high_score.txt') as f:
            self.high_score = int(f.read())
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that change during the game"""
        self.score = 0
        self.level = 1

