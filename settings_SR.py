import pygame

class Settings:
    """A class to store all settings for SRNW"""

    def __init__(self):
        """Initialize the SRNW's settings"""

        #screen settings
        self.dirt = pygame.image.load('images/tile_0034.png')
        self.dirt_rect = self.dirt.get_rect()
        self.tile_size = self.dirt_rect.width
        self.screen = pygame.display.set_mode((40 * self.tile_size, 40 * self.tile_size))
        self.screen_rect = self.screen.get_rect()
        self.rows = self.screen_rect.height // self.tile_size
        self.cols = self.screen_rect.width // self.tile_size
        self.bg_color = (242, 106, 15)

        #Wave settings
        #self.wave_speed = 1
        self.wave_drop_speed = 5
        self.wave_direction = 1
        self.wave_direction2 = 1
        self.wave_direction3 = 1
        self.wave_direction4 = 1

        #Crab Tank settings
        #self.tank_speed = 1
        self.tank_limit = 3

        #Bullet settings
        #self.bullet_speed = 3
        self.bullet_width = 1000
        self.bullet_height = 10
        self.bullet_color = (0, 0, 255)
        self.bullets_allowed = 10

        #Increase the game's speed for each wave defeated
        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()

        #Music
        self.track1 = pygame.mixer.music.load('music/Deluge_Dirge.oga', "oga")

    def initialize_dynamic_settings(self):
        """Settings that change over the course of gameplay"""
        self.tank_speed = 1.25
        self.bullet_speed = 3
        self.wave_speed = 1
        self.chum_points = 10
        self.cohock_points = 50
        self.goldie_points = 200
        self.smallfry_points = 5
        self.wave_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.tank_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.wave_speed *= self.speedup_scale

    def better_bullets(self):
        """Increase the size of bullets"""
        self.bullet_width += 2
        self.bullets_allowed += 5


