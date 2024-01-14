import pygame
from pygame.sprite import Sprite


class EnemyShip(Sprite):
    def __init__(self, ui_game):
        super().__init__()
        self.screen = ui_game.game_screen
        self.settings = ui_game.settings

        self.image = ui_game.settings.enemy_ship_scaled
        self.rect = self.image.get_rect()

        # Start each new enemy ship near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the enemies exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.enemy_ship_speed * self.settings.fleet_direction)
        self.rect.x = self.x
