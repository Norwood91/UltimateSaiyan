import pygame
from pygame.sprite import Sprite


class EnergyBlast(Sprite):
    def __init__(self, ui_game):
        super().__init__()
        self.screen = ui_game.game_screen
        self.settings = ui_game.settings

        # Load the blast image and get it's rectangle
        self.energy_blast = self.settings.blast_image_scaled
        self.rect = self.energy_blast.get_rect()

        # Set the starting position of the blast
        self.rect.midtop = ui_game.main_character_ship.rect.midtop

        # Store decimal value for the vertical position of the bullet(s)
        self.y = float(self.rect.y)


    def update(self):
        # Update the decimal position of the bullet
        self.y -= self.settings.blast_speed

        # Update the position of the rect
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.energy_blast, self.rect)

