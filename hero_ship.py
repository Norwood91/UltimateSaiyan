import pygame


class Hero:
    # Init takes two params, self and a reference to the current instance of the Ultimate Saiyan class
    def __init__(self, ui_game):
        """Initialize the hero ship and it's starting position"""
        self.screen = ui_game.game_screen
        self.screen_rect = ui_game.game_screen.get_rect()

        # Load the ship image, get its rectangle, and resize the image
        self.goku_image = pygame.image.load('images/goku_ship.bmp')
        self.goku_image = pygame.transform.scale(self.goku_image, (30, 30))
        self.rect = self.goku_image.get_rect()

        # Start each new ship at the specified coordinates
        self.rect.x = 600
        self.rect.y = 740

        # Movement Flag(s)
        self.moving_right = False

    def update_movement(self):
        """Updates the position of the ship based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1


    def blitme(self):
        """Draw the ship at its current position onto the screen"""
        self.screen.blit(self.goku_image, (self.rect.x, self.rect.y))
