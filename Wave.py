import pygame

class Wave:
    """A class for a single Chum in the run."""
    def __init__(self, sr_game):
        """Initialize the chum and set its starting position."""

        self.screen = sr_game.screen
        self.image = pygame.image.load('../images/Chum.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.chum_speed = 1
        self.wave_direction = 1

    def update(self):
        """Move the chum to the right."""
        self.x += (self.chum_speed * self.wave_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if chum is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True