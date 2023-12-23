import pygame


class Settings:
    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.main_screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (0, 0, 135)
        self.screen_title = "Ultimate Saiyan"

        # Hero Ship Settings
        self.hero_ship_speed = 2
        self.hero_image = pygame.image.load('images/goku_ship.bmp')
        self.scaled_hero_image = pygame.transform.scale(self.hero_image, (30, 30))
        self.starting_heroes_x_position = 600
        self.starting_hereos_y_position = 740
