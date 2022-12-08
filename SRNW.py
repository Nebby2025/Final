
import sys
import pygame
import time
from settings_SR import Settings
from Wave import Wave
from Tank import Tank
from ink import Bullet
from sr_stats import GameStats
from score import Scoreboard
from Cohock import Wave2
from Goldie import Wave3
from Smallfry import Wave4
from timer import Timer

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
        self.wave2 = pygame.sprite.Group()
        self.wave3 = pygame.sprite.Group()
        self.wave4 = pygame.sprite.Group()
        self.bullet = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.score = Scoreboard(self)
        self.timer = Timer(self)
        self.clock = pygame.time.Clock()
        self._create_wave_3()


    def run_game(self):
        """Initializing game loop..."""
        while True:
            self._check_events()
            if self.stats.game_active:
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
            with open('high_score.txt', 'w', encoding = 'utf-8') as file:
                file.write(f'{self.stats.high_score}')
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.tank.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.tank.moving_right = False
        elif event.key == pygame.K_SPACE:
            self.tank.firing = False

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

        self._check_bullet_salmonid_collisions()

    def _check_bullet_salmonid_collisions(self):
        """Respond to bullet-chum collisions"""
        #Check for any bullets have hit a chum
        #If hit, delete both
        collisions = pygame.sprite.groupcollide(self.bullet, self.wave, True, True)
        collisions2 = pygame.sprite.groupcollide(self.bullet, self.wave2, True, True)
        collisions3 = pygame.sprite.groupcollide(self.bullet, self.wave3, True, True)
        collisions4 = pygame.sprite.groupcollide(self.bullet, self.wave4, True, True)

        if collisions:
            for chum in collisions.values():
                self.stats.score += self.settings.chum_points * len(chum)
            self.score.prep_score()
            self.score.check_high_score()

        if collisions2:
            for cohock in collisions2.values():
                self.stats.score += self.settings.cohock_points * len(cohock)
            self.score.prep_score()
            self.score.check_high_score()

        if collisions3:
            for goldie in collisions3.values():
                self.stats.score += self.settings.goldie_points * len(goldie)
            self.score.prep_score()
            self.score.check_high_score()

        if collisions4:
            for smallfry in collisions4.values():
                self.stats.score += self.settings.smallfry_points * len(smallfry)
            self.score.prep_score()
            self.score.check_high_score()

    def _increase_wave_number(self):
        #Increase the Wave number
        self.stats.level += 1
        self.score.prep_level()



    def _update_wave(self):
        """Check if the wave is at an edge, then change its position"""
        self._check_wave_edges()
        #self._check_wave_size()
        self._check_time_left()
        self.wave.update()
        self.wave2.update()
        self.wave3.update()
        self.wave4.update()
        #print(self.timer.timer)

    # def _check_wave_size(self):
    #      if len(self.wave2) + len(self.wave) < 20:
    #          self._check_wave_number()

    def _check_time_left(self):
        if self.timer.timer <= 0:
            self._rest()
            self._increase_wave_number()
            # self.timer.reset_clock()
            # self.timer.run_clock()

    def _rest(self):
        self.wave2.empty()
        self.wave.empty()
        self.bullet.empty()
        self.timer.reset()
        time.sleep(0.5)

    def _check_wave_number(self):
        self.stats.random_number()
        if self.stats.rn <= 3:
            self._create_wave()
        else:
            self._create_wave_2()



    def _check_wave_edges(self):
        """Check if wave hits the edge of the screen"""
        for chum in self.wave.sprites():
            if chum.check_edges():
                self._change_wave_direction()
                break
        for cohock in self.wave2.sprites():
            if cohock.check_edges():
                self._change_wave_direction2()
                break
        for goldie in self.wave3.sprites():
            if goldie.check_edges():
                self._change_wave_direction3()
                break
        for smallfry in self.wave4.sprites():
            if smallfry.check_edges():
                self._change_wave_direction4()
                break

    def _change_wave_direction(self):
        """Respond if any of the Chum have reached the screen's edge"""
        for chum in self.wave.sprites():
            chum.rect.y += self.settings.wave_drop_speed
        self.settings.wave_direction *= -1

    def _change_wave_direction2(self):
        for cohock in self.wave2.sprites():
            cohock.rect.y += self.settings.wave_drop_speed
        self.settings.wave_direction *= -1

    def _change_wave_direction3(self):
        for goldie in self.wave3.sprites():
            goldie.rect.y += self.settings.wave_drop_speed
        self.settings.wave_direction *= -1

    def _change_wave_direction4(self):
        for smallfry in self.wave4.sprites():
            smallfry.rect.y += self.settings.wave_drop_speed
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
        chum.rect.y = chum_height + (2 * chum.rect.height * row_number)
        self.wave.add(chum)

    def _create_cohock(self, co_number, row_number2):
        cohock = Wave2(self)
        cohock_width, cohock_height = cohock.rect.size
        cohock.x = cohock_width + (2 * cohock_width * co_number)
        cohock.rect.x = cohock.x
        cohock.rect.y = cohock_height + (2 * cohock.rect.height * row_number2)
        self.wave2.add(cohock)

    def _create_goldie(self, g_number, row_number3):
        goldie = Wave3(self)
        goldie_width, goldie_height = goldie.rect.size
        goldie.x = goldie_width + (2 * goldie_width * g_number)
        goldie.rect.x = goldie.x
        goldie.rect.y = goldie_height + (2 * goldie.rect.height * row_number3)
        self.wave3.add(goldie)

    def _create_smallfry(self, sf_number, row_number4):
        smallfry = Wave4(self)
        smallfry_width, smallfry_height = smallfry.rect.size
        smallfry.x = smallfry_width (2 * smallfry_width * sf_number)
        smallfry.rect.x = smallfry.x
        smallfry.rect.y = smallfry_height + (2 * smallfry.rect.height * row_number4)
        self.wave4.add(smallfry)


    def _create_wave(self):
        chum = Wave(self)
        chum_width, chum_height = chum.rect.size
        available_space_x = self.settings.screen_rect.width - (1 * chum_width)
        number_chum_x = available_space_x // (2 * chum_width)

        #Limit the wave
        available_space_y = (self.settings.screen_rect.height - (2 * chum_height))
        number_rows = available_space_y // (4 * chum_height)

        for row_number in range(number_rows):
            for chum_number in range(number_chum_x):
                self._create_chum(chum_number, row_number)

    def _create_wave_2(self):
        cohock = Wave2(self)
        cohock_width, cohock_height = cohock.rect.size
        available_space_x2 = self.settings.screen_rect.width - (1 * cohock_width)
        number_cohock_x = available_space_x2 // (2 * cohock_width)

        # Limit the wave
        available_space_y2 = (self.settings.screen_rect.height - (2 * cohock_height))
        number_rows2 = available_space_y2 // (3 * cohock_height)

        for row_number2 in range(number_rows2):
            for co_number in range(number_cohock_x):
                self._create_cohock(co_number, row_number2)

    def _create_wave_3(self):
        goldie = Wave3(self)
        goldie_width, goldie_height = goldie.rect.size
        available_space_x3 = self.settings.screen_rect.width - (2 * goldie_width)
        number_goldie_x = available_space_x3 // (2 * goldie_width)

        available_space_y3 = (self.settings.screen_rect.height - (2 * goldie_height))
        number_rows3 = available_space_y3 // (3 * goldie_height)

        for row_number3 in range(number_rows3):
            for g_number in range(number_goldie_x):
                self._create_goldie(g_number, row_number3)

    def _create_wave_4(self):
        smallfry = Wave4(self)
        smallfry_width, smallfry_height = smallfry.rect.size
        available_space_x4 = self.settings.screen_rect.width - (2 * smallfry_width)
        number_smallfry_x = available_space_x4 // (1 * smallfry_width)

        available_space_y4 = (self.settings.screen_rect.height - (5 * smallfry_height))
        number_rows4 = available_space_y4 // (3 * smallfry_height)

        for row_number4 in range(number_rows4):
            for sf_number in range(number_smallfry_x):
                self._create_smallfry(sf_number, row_number4)

    def _update_screen(self):
        self._draw_background()
        self.tank.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.wave.draw(self.settings.screen)
        self.wave2.draw(self.settings.screen)
        self.wave3.draw(self.settings.screen)
        self.wave4.draw(self.settings.screen)
        self.score.show_score()
        self.timer.run_clock()
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    sr = SRNW()
    sr.run_game()