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
        self.timer = 20
        self.dt = 0
        self.font = pygame.font.Font(None, 40)
        self.color = pygame.Color('dodgerblue')
        self.clock = pygame.time.Clock()
        #self.txt = self.font.render(str(round(self.timer, 2)), True, self.color)

        self.run_clock()

    def run_clock(self):
        """Let time begin..."""

        self.timer -= self.dt
        if self.timer >= 0:
            # self.timer -= self.dt
            self.txt = self.font.render(str(round(self.timer, 0)), True, self.color)
            self.screen.blit(self.txt, (150, 0))
            self.dt = self.clock.tick(240) / 1000



