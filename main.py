import sys
import pygame
from settings import Settings
from hero_ship import Hero


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

    def run_game(self):
        """Starts the main loop of the game"""
        while True:
            self._check_events()
            self.main_character_ship.update_movement()
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

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.main_character_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.main_character_ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.main_character_ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.main_character_ship.moving_up = False

    def _update_screen(self):
        """Updates images onto the screen, and flips to the new screen"""
        # Redraw the screen during each pass of the while loop
        self.game_screen.fill(self.settings.bg_color)
        # Draw the hero ship to the screen, on top of the background
        self.main_character_ship.blitme()
        # Make the most recently drawn screen visible. Draws an empty screen on each pass through the while loop,
        # erasing the old screen so only the new one is visible
        pygame.display.flip()


if __name__ == '__main__':
    ui = UltimateSaiyan()
    ui.run_game()
