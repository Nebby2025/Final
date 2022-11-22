import pygame


class Tank:
    """Class for the player"""
    def __init__(self, sr_game):
        """Initialize the Crab Tank and set its starting position"""

        self.screen = sr_game.screen
        self.screen_rect = sr_game.screen.get_rect()
        self.settings = sr_game.settings

        #Load Crab Tank and get its rect
        self.image = pygame.image.load('images/Crab_Tank.png')
        self.rect = self.image.get_rect()

        #Start each new Crab Tank at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the Crab Tank's position
        self.x = float(self.rect.x)

        #Movement flags
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Updates the Crab Tank's position based on movement flags"""
        #Update the CT's x value, not its rect.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.tank_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.tank_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the CT at its current location"""

        self.screen.blit(self.image, self.rect)

    def center_tank(self):
        """Center the CT on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
