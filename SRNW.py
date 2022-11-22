import sys
import pygame
from settings_SR import Settings
from Wave import Wave
from Tank import Tank
from ink import Bullet

class SRNW:
    """Overall class to manage game assests and behaviour."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption("The Next Wave")
        self.screen = self.settings.screen

        self.bg_color = (255, 34, 123)

        #Game characteristics (add here after importing a class)
        self.tank = Tank(self)
        self.wave = pygame.sprite.Group()
        self.bullet = pygame.sprite.Group()
        self._create_wave()

    def run_game(self):
        """Initializing game loop..."""
        while True:
            self._check_events()
            self.tank.update()
            self._update_bullets()
            self._update_wave()
            self._update_screen()

    def _check_events(self):
        """Respond to inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_LEFT:
            self.tank.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.tank.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.tank.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.tank.moving_right = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullet) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _update_bullets(self):
        """Update the position of bullets and delete old bullets"""
        #Update bullet position
        self.bullet.update()

        # Get rid of bullets that are not on screen
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)

        self._check_bullet_chum_collisions()

    def _check_bullet_chum_collisions(self):
        """Respond to bullet-chum collisions"""
        #Check for any bullets have hit a chum
        #If hit, delete both
        collisions = pygame.sprite.groupcollide(self.bullet, self.wave, True, True)

        if not self.wave:
            #Destroy existing bullets and create a new wave
            self.bullet.empty()
            self._create_wave()
            self.settings.better_bullets()
            self.settings.increase_speed()

    def _update_wave(self):
        """Check if the wave is at an edge, then change its position"""
        self._check_wave_edges()
        self.wave.update()

    def _check_wave_edges(self):
        """Check if wave hits the edge of the screen"""
        for chum in self.wave.sprites():
            if chum.check_edges():
                self._change_wave_direction()
                break

    def _change_wave_direction(self):
        """Respond if any of the Chum have reached the screen's edge"""
        for chum in self.wave.sprites():
            chum.rect.y += self.settings.wave_drop_speed
        self.settings.wave_direction *= -1


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
        available_space_x = self.settings.screen_rect.width - (1 * chum_width)
        number_chum_x = available_space_x // (2 * chum_width)

        #Limit the wave
        available_space_y = (self.settings.screen_rect.height - (9 * chum_height))
        number_rows = available_space_y // (4 * chum_height)

        for row_number in range(number_rows):
            for chum_number in range(number_chum_x):
                self._create_chum(chum_number, row_number)

    def _update_screen(self):
        self._draw_background()
        self.tank.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.wave.draw(self.settings.screen)
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    sr = SRNW()
    sr.run_game()