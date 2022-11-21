import pygame
from settings_SR import Settings
from Wave import Wave

class SRNW:
    """Overall class to manage game assests and behaviour."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption("The Next Wave")

        self.bg_color = (255, 34, 123)

        #Game characteristics
        self.wave = pygame.sprite.Group()

    def run_game(self):
        """Initializing game loop..."""
        while True:
            #self._draw_background()
            self._update_screen()


    def _draw_background(self):
        #Draw the background for the game
        for x in range(int(self.settings.rows)):
            for y in range(int(self.settings.cols)):
                self.settings.screen.blit(self.settings.dirt, (x*self.settings.dirt_rect.height, y*self.settings.dirt_rect.width))

    def _create_chum(self, chum_number, row_number):
        chum = Wave(self)
        chum_width, chum_height = chum.rect.size
        chum.x = chum_width + (2 * chum_width * chum_number)
        chum.rect.x = chum.x
        chum.rect.y = chum_height + 2 * chum.rect.height * row_number
        self.wave.add(chum)

    def _create_wave(self):
        chum = Wave(self)
        chum_width, chum_height = chum.rect.size
        available_space_x = self.settings.screen_rect.width - (2 * chum_width)
        number_chum_x = available_space_x // (2 * chum_width)

        #Limit the wave
        available_space_y = (self.settings.screen_rect.height - (2 * chum_height))
        number_rows = available_space_y // (2 * chum_height)

        for row_number in range(number_rows):
            for chum_number in range(number_chum_x):
                self._create_chum(chum_number, row_number)

    def _update_screen(self):
        self.wave.draw(self.settings.screen)
        self._draw_background()
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    sr = SRNW()
    sr.run_game()