import pygame

class Settings:
    """A class to store all settings for SRNW"""

    def __init__(self):
        """Initialize the SRNW's settings"""

        #screen settings
        self.dirt = pygame.image.load('images/tile_0034.png')
        self.dirt_rect = self.dirt.get_rect()
        self.tile_size = self.dirt_rect.width
        self.screen = pygame.display.set_mode((30 * self.tile_size, 30 * self.tile_size))
        self.screen_rect = self.screen.get_rect()
        self.rows = self.screen_rect.height // self.tile_size
        self.cols = self.screen_rect.width // self.tile_size

        #Wave settings
        self.wave_speed = 1
        self.wave_drop_speed = 10
        self.wave_direction = 1