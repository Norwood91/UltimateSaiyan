import pygame

class Settings:
    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1334
        self.screen_height = 750
        self.main_screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_image = pygame.image.load('images/background_image.webp')
        self.screen_title = "Ultimate Saiyan"

        # Hero Ship Settings
        self.hero_ship_speed = 1.5
        self.hero_image = pygame.image.load('images/goku_ship.bmp')
        self.scaled_hero_image = pygame.transform.scale(self.hero_image, (30, 30))

        # Enemy Ship Settings
        self.enemy_ship = pygame.image.load('images/enemy_ship.png')
        self.enemy_ship_scaled = pygame.transform.scale(self.enemy_ship, (40, 40))

        # Ki-Blast Settings
        self.blast_speed = 1
        self.blasts_allowed = 3
        self.blast_image = pygame.image.load('images/energy_blast.png')
        self.blast_image_scaled = pygame.transform.scale(self.blast_image, (20, 20))