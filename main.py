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

        # Main Game Screen
        self.game_screen = self.settings.main_screen
        pygame.display.set_caption(self.settings.screen_title)

        # Main Character Ship
        self.main_character_ship = Hero(self)

        # Energy Blast(s)
        self.energy_blasts = pygame.sprite.Group()

        # Enemy Ships
        self.frieza_force = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Starts the main loop of the game"""
        while True:
            self._check_events()
            self.main_character_ship.update_movement()
            self._update_blasts()
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
            # Create a new blast and add it to the blasts group
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

    def _create_fleet(self):
        enemy_ship = EnemyShip(self)
        enemy_ship_width = enemy_ship.rect.width
        horizontal_screen_space = self.settings.screen_width - (2 * enemy_ship_width)
        num_enemies_in_horizontal_row = horizontal_screen_space // (2 * enemy_ship_width)

        # Create the first row of enemy ships
        for ship_number in range(num_enemies_in_horizontal_row):
            # Instantiate a new instance of the Enemies class
            enemy = EnemyShip(self)
            # Get the x-coordinate for the ship
            enemy.x = enemy_ship_width + (2 * enemy_ship_width) * ship_number

            #print(f'Ship number: {ship_number} has an x-coord of: {enemy.x}')

            # Start the next enemy 80 pixels to the right of the previous ship
            enemy.rect.x = enemy.x
            # Add the enemy to the frieza force group
            self.frieza_force.add(enemy)

    def _update_screen(self):
        """Updates images onto the screen, and flips to the new screen"""
        self.game_screen.blit(self.settings.bg_image, (0, 0))
        self.main_character_ship.blitme()
        self.frieza_force.draw(self.game_screen)
        self._display_blast()
        pygame.display.flip()


if __name__ == '__main__':
    ui = UltimateSaiyan()
    ui.run_game()
