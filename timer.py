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

    def prep_clock(self):
        """Turn the score into a rendered image"""
        clock = pygame.time.Clock
        clock_str = "{:.}".format(clock)
        self.clock_image = self.font.render(clock_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right of the screen
        self.clock_rect = self.clock_image.get_rect()
        self.clock_rect.midtop = self.screen_rect.midtop
        self.clock_rect.top = 20

    def show_clock(self):
        """Draw the clock to the screen"""
        self.screen.blit(self.clock_image, self.clock_rect)

    def run_clock(self):
        """Changes the time remaining"""
        self.timer = 100
        self.dt = 0
        self.timer -= self.dt
        if self.timer <= 0:
            txt = font.render('Game Over!', True, blue)
            # timer = 10  # Reset it to 10 or do something else.
        else:
            txt = font.render(str(round(self.timer, 2)), True, blue)