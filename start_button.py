

class StartButton:
    def __init__(self, ui_game):
        self.screen = ui_game.game_screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ui_game.settings

        self.button = self.settings.button_image_scaled
        self.rect = self.button.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.button, self.rect)