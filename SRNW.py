import pygame
from settings_SR import Settings

class SRNW:
    """Overall class to manage game assests and behaviour."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((800, 600))
        # self.dirt = pygame.image.load('../images/tile_0034.png')
        # self.dirt_rect = self.dirt.get_rect()
        # self.tile_size = self.dirt_rect.width
        # self.screen = pygame.display.set_mode((30*self.tile_size, 30*self.tile_size))
        # self.screen_rect = self.screen.get_rect()
        # self.rows = self.screen_rect.height//self.tile_size
        # self.cols = self.screen_rect.width//self.tile_size
        pygame.display.set_caption("The Next Wave")

        self.bg_color = (255, 34, 123)

    def run_game(self):
        """Initializing game loop..."""
        while True:
            self._draw_background()
            pygame.display.flip()


    def _draw_background(self):
        #Draw the background for the game
        for x in range(int(self.rows)):
            for y in range(int(self.cols)):
                self.screen.blit(self.dirt, (x*self.dirt_rect.height, y*self.dirt_rect.width))

if __name__ == '__main__':
    #Make a game instance, and run the game
    sr = SRNW()
    sr.run_game()