import pygame

class Hero:
    # Init takes two params, self and a reference to the current instance of the Ultimate Saiyan class
    def __init__(self, ui_game):
        """Initialize the hero ship and it's starting position"""
        self.screen = ui_game.game_screen
        self.screen_rect = ui_game.game_screen.get_rect()
        self.settings = ui_game.settings

        # Load the ship image and get its rectangle
        self.hero_ship_image = ui_game.settings.scaled_hero_image
        self.rect = self.hero_ship_image.get_rect()

        # Start each new ship at the specified coordinates
        self.rect.x = self.settings.starting_heroes_x_position
        self.rect.y = self.settings.starting_hereos_y_position

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement Flag(s)
        self.moving_right = False
        self.moving_left = False

    def update_movement(self):
        """Updates the position of the ship based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Updates the ship's x value instead of the rect's x value
            self.x += self.settings.hero_ship_speed

        if self.moving_left and self.rect.left > 0:
            # Updates the ship's x value instead of the rect's x value
            self.x -= self.settings.hero_ship_speed

        # Update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current position onto the screen"""
        self.screen.blit(self.hero_ship_image, (self.rect.x, self.rect.y))
