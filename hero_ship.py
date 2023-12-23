import pygame


class Hero:
    # Init takes two params, self and a reference to the current instance of the Ultimate Saiyan class
    def __init__(self, ui_game):
        """Initialize the hero ship and it's starting position"""
        self.screen = ui_game.game_screen
        self.screen_rect = ui_game.game_screen.get_rect()

        # Load the ship image and get its rectangle
        self.goku_image = pygame.image.load('images/goku_ship.png')
        self.rect = self.goku_image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current position onto the screen"""
        self.screen.blit(self.goku_image, self.rect)
