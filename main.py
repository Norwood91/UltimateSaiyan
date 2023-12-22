import sys

import pygame


class UltimateSaiyan:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Ultimate Saiyan')

    def run_game(self):
        """Starts the main loop of the game"""
        while True:
            # Watch for keyboard and mouse events
            # Returns a list of events that have taken place since the last time the run_game function was called
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible. Draws an empty screen on each pass through the while loop,
            # erasing the old screen so only the new one is visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make an instance of the game, and run the game.
    ui = UltimateSaiyan()
    ui.run_game()
