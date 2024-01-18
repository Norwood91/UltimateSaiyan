from pygame.sprite import Sprite
class Hero(Sprite):
    def __init__(self, ui_game):
        super().__init__()
        """Initialize the hero ship and it's starting position"""
        self.screen = ui_game.game_screen
        self.screen_rect = ui_game.game_screen.get_rect()
        self.settings = ui_game.settings

        # Load the ship image and get its rectangle
        self.image = ui_game.settings.scaled_hero_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)

        # Movement Flag(s)
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update_movement(self):
        """Updates the position of the ship based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.hero_ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.hero_ship_speed

        if self.moving_down and self.rect.bottom <= 748:
            self.y += self.settings.hero_ship_speed

        if self.moving_up and self.rect.top >= 3:
                self.y -= self.settings.hero_ship_speed

        # Update the rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Centers the hero ship on the screen"""
        self.x = 650
        self.y = 720

    def blitme(self):
        """Draw the ship at its current position onto the screen"""
        self.screen.blit(self.image, self.rect)
