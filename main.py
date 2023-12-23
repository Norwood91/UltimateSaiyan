import sys
import pygame
from settings import Settings
from hero_ship import Hero


class UltimateSaiyan:
    """Class to manage game assets and behavior"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # Screen Settings
        self.game_screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.screen_title)

        # Hero Ship
        # The self here gives our hero ship access to the game's resources like the screen object
        self.goku_ship = Hero(self)

    def run_game(self):
        """Starts the main loop of the game"""
        while True:
            # Watch for keyboard and mouse events
            # Returns a list of events that have taken place since the last time the run_game function was called
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass of the while loop
            self.game_screen.fill(self.settings.bg_color)
            # Draw the hero ship to the screen, on top of the background
            self.goku_ship.blitme()

            # Make the most recently drawn screen visible. Draws an empty screen on each pass through the while loop,
            # erasing the old screen so only the new one is visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make an instance of the game, and run the game.
    ui = UltimateSaiyan()
    ui.run_game()
