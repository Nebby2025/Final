import pygame

class Timer:
    """A class for a timer"""

    def __init__(self, sr_game):
        """Initialize clock"""

        self.screen = sr_game.screen
        self.screen_rect = sr_game.screen.get_rect()
        self.settings = sr_game.settings

        # Font settings for clock info
        self.text_color = (241, 94, 80)
        self.font = pygame.font.SysFont('comicsansms', 25)

        #Other clock settings
        self.timer = 100
        self.dt = 0
        self.font = pygame.font.Font(None, 40)
        self.color = pygame.Color('dodgerblue')
        self.clock = pygame.time.Clock

        self.prep_clock()

    def prep_clock(self):
        """Turn the score into a rendered image"""

        self.clock_image = self.font.render(self.clock, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right of the screen
        self.clock_rect = self.clock_image.get_rect()
        self.clock_rect.midtop = self.screen_rect.midtop
        self.clock_rect.top = 20

    def show_clock(self):
        """Draw the clock to the screen"""
        self.screen.blit(self.clock_image, self.clock_rect)

    def run_clock(self):
        """Changes the time remaining"""
        self.timer -= self.dt
        if self.timer <= 0:
            txt = self.font.render('Game Over!', True, self.color)
            # timer = 10  # Reset it to 10 or do something else.
        else:
            txt = self.font.render(str(round(self.timer, 2)), True, self.color)