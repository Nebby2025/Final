import pygame.font

class Scoreboard:
    """A class to report the score"""

    def __init__(self, sr_game):
        """Initialize scorekeeping attributes"""
        self.screen = sr_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sr_game.settings
        self.stats = sr_game.stats

        #Font settings for score info
        self.text_color = (41, 194, 46)
        self.font = pygame.font.SysFont('comicsansms', 25)

        #Prepare the initial score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        score = int(self.stats.score)
        score_str = "{:,}".format(score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """Turn the highest score into an image"""
        high_score = int(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 10
        self.high_score_rect.top = 20