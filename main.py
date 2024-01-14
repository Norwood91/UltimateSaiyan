import sys
import pygame
from settings import Settings
from hero_ship import Hero
from energy_blast import EnergyBlast
from frieza_force import EnemyShip


class UltimateSaiyan:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.game_screen = self.settings.main_screen
        pygame.display.set_caption(self.settings.screen_title)

        self.main_character_ship = Hero(self)

        self.energy_blasts = pygame.sprite.Group()

        self.f_force = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Starts the main loop of the game"""
        while True:
            self._check_events()
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

    def _update_enemy_ships(self):
        self._check_fleet_edges()
        self.f_force.update()

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
        self.main_character_ship.blitme()
        self.f_force.draw(self.game_screen)
        self._display_blast()
        pygame.display.flip()


if __name__ == '__main__':
    ui = UltimateSaiyan()
    ui.run_game()
