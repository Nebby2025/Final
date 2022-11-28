import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the CT"""

    def __init__(self, sr_game):
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = sr_game.tank.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        #Set a flag for shooting
        self.shooting = False

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
