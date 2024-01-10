import pygame
from pygame.sprite import Sprite


class EnemyShip(Sprite):
    def __init__(self, ui_game):
        super().__init__()
        self.screen = ui_game.game_screen

        self.image = ui_game.settings.enemy_ship_scaled
        self.rect = self.image.get_rect()

        # Start each new enemy ship near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the enemies exact horizontal position
        self.x = float(self.rect.x)
