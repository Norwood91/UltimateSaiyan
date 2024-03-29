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

        # Game Settings
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # Start Button Settings
        self.button_image = pygame.image.load("images/start_button.png")
        self.button_image_scaled = pygame.transform.scale(self.button_image, (300, 300))

        # Hero Ship Settings
        self.hero_ship_limit = 3
        self.hero_image = pygame.image.load('images/goku_ship.bmp')
        self.scaled_hero_image = pygame.transform.scale(self.hero_image, (30, 30))

        # Enemy Ship Settings
        self.enemy_ship = pygame.image.load('images/enemy_ship.png')
        self.enemy_ship_scaled = pygame.transform.scale(self.enemy_ship, (40, 40))
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Ki-Blast Settings
        self.blasts_allowed = 3
        self.blast_image = pygame.image.load('images/energy_blast.png')
        self.blast_image_scaled = pygame.transform.scale(self.blast_image, (20, 20))

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.hero_ship_speed = 1.5
        self.blast_speed = 2
        self.enemy_ship_speed = 1
        self.fleet_direction = 1
        self.enemy_shot_points = 50

    def increase_speed(self):
        """Increase the speed and point settings"""
        self.hero_ship_speed *= self.speedup_scale
        self.blast_speed *= self.speedup_scale
        self.enemy_ship_speed *= self.speedup_scale
        self.enemy_shot_points = int(self.enemy_shot_points * self.score_scale)