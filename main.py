import sys
from time import sleep
import pygame
from settings import Settings
from hero_ship import Hero
from energy_blast import EnergyBlast
from frieza_force import EnemyShip
from game_stats import GameStats
from start_button import StartButton
from scoreboard import Scoreboard


class UltimateSaiyan:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.game_screen = self.settings.main_screen
        pygame.display.set_caption(self.settings.screen_title)
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.main_character_ship = Hero(self)
        self.energy_blasts = pygame.sprite.Group()
        self.f_force = pygame.sprite.Group()
        self._create_fleet()
        self.start_button = StartButton(self)

    def run_game(self):
        """Starts the main loop of the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.main_character_ship.update_movement()
                self._update_blasts()
                self._update_enemy_ships()
            self._update_screen()

    def _check_events(self):
        """Responds to key presses and mouse events"""
        # Returns a list of events that have taken place since the last time the run_game function was called
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_start_button(mouse_pos)

    def _check_start_button(self, mouse_pos):
        start_button_clicked = self.start_button.rect.collidepoint(mouse_pos)
        if start_button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.scoreboard.prep_game_level()
            self.f_force.empty()
            self.energy_blasts.empty()
            self._create_fleet()
            self.main_character_ship.center_ship()
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.main_character_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.main_character_ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.main_character_ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.main_character_ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_blast()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.main_character_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.main_character_ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.main_character_ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.main_character_ship.moving_up = False

    def _fire_blast(self):
        if len(self.energy_blasts) < self.settings.blasts_allowed:
            new_blast = EnergyBlast(self)
            self.energy_blasts.add(new_blast)

    def _display_blast(self):
        for blast in self.energy_blasts.sprites():
            blast.blitme()

    def _update_blasts(self):
        self.energy_blasts.update()
        for blast in self.energy_blasts.copy():
            if blast.rect.bottom <= 0:
                self.energy_blasts.remove(blast)
        self._check_blast_enemy_collision()

    def _check_blast_enemy_collision(self):
        collisions = pygame.sprite.groupcollide(self.energy_blasts, self.f_force, False, True)
        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_shot_points * len(enemies)
                self.scoreboard.prep_score()
                self.scoreboard.check_high_score()

        if not self.f_force:
            self.energy_blasts.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.game_level += 1
            self.scoreboard.prep_game_level()
            self.scoreboard.check_high_level()

    def _check_enemies_hit_bottom(self):
        """Check if any enemy ships have reached the bottom of screen"""
        screen_rect = self.game_screen.get_rect()
        for enemy in self.f_force.sprites():
            if enemy.rect.bottom >= screen_rect.bottom:
                self._hero_ship_hit()
                break

    def _update_enemy_ships(self):
        self._check_fleet_edges()
        self.f_force.update()

        if pygame.sprite.spritecollideany(self.main_character_ship, self.f_force):
            self._hero_ship_hit()

        self._check_enemies_hit_bottom()

    def _hero_ship_hit(self):
        """Responds to the hero ship being hit by an alien"""
        if self.stats.hero_ships_left > 0:
            self.stats.hero_ships_left -= 1
            self.f_force.empty()
            self.energy_blasts.empty()

            self._create_fleet()
            self.main_character_ship.center_ship()
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        enemy_ship = EnemyShip(self)
        enemy_width, enemy_height = enemy_ship.rect.size
        horizontal_screen_space = self.settings.screen_width - (2 * enemy_width)
        num_enemies_in_horizontal_row = horizontal_screen_space // (2 * enemy_width)

        hero_ship_height = self.main_character_ship.rect.height
        vertical_screen_space = (self.settings.screen_height - (3 * enemy_height) - hero_ship_height)
        num_of_vert_rows = vertical_screen_space // (2 * enemy_height)

        # Create the fleet of enemy ships
        for row_number in range(num_of_vert_rows):
            for ship_number in range(num_enemies_in_horizontal_row):
                self._create_enemy(ship_number, row_number)

    def _create_enemy(self, ship_number, row_number):
        """Create alien and place it in the row"""
        enemy = EnemyShip(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.x = enemy_width + (2 * enemy_width) * ship_number
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy_height + (1.25 * enemy.rect.height) * row_number
        self.f_force.add(enemy)

    def _check_fleet_edges(self):
        for enemy in self.f_force.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for enemy in self.f_force.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Updates images onto the screen, and flips to the new screen"""
        self.game_screen.blit(self.settings.bg_image, (0, 0))
        if not self.stats.game_active:
            self.start_button.blitme()
        else:
            self.scoreboard.show_score()
            self.main_character_ship.blitme()
            self.f_force.draw(self.game_screen)
            self._display_blast()

        pygame.display.flip()


if __name__ == '__main__':
    ui = UltimateSaiyan()
    ui.run_game()
