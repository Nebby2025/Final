import pygame
from pygame.sprite import Sprite

class Wave3(Sprite):
    """A class for a single Goldie in the run."""
    def __init__(self, sr_game):
        """Initialize the goldie and set its starting position."""
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings
        self.image = pygame.image.load('images/goldie.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move the wave to the right."""
        self.x += (self.settings.wave_speed * self.settings.wave_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if goldie is at the edge of the screen."""
        screen_rect = self.settings.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True