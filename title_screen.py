import pygame.font

class TitleScreen:
    """Class to display the title screen of the game"""
    def __init__(self, ui_game):
        self.screen = ui_game.game_screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ui_game.settings
        self.prep_game_logo()
        self.prep_title_string()
        self.prep_secondary_title_string()
        self.prep_title_footer()
        self.prep_instructions()


    def prep_game_logo(self):
        self.game_logo = pygame.image.load('images/game_logo.png')
        self.game_logo_rect = self.game_logo.get_rect()
        self.game_logo_rect.centerx = self.screen_rect.centerx
        self.game_logo_rect.y = 45

    def prep_title_string(self):
        text_color = (214, 119, 17)
        font = pygame.font.SysFont('Times New Roman', 100)
        title_str = 'Ultimate Saiyan'
        self.title_image = font.render(title_str, True, text_color)
        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.y = float(self.screen_rect.height * .42)

    def prep_secondary_title_string(self):
        text_color = (255, 255, 255)
        font = pygame.font.SysFont("Apple Garamond", 34)
        self.sec_title_str = 'Protect Planet Vegeta from the Ferocious Frieza Force!'
        self.sec_title_image = font.render(self.sec_title_str, True, text_color)
        self.sec_title_rect = self.sec_title_image.get_rect()
        self.sec_title_rect.centerx = self.screen_rect.centerx
        self.sec_title_rect.y = float(self.screen_rect.height * .57)

    def prep_instructions(self):
        text_color = (255, 255, 255)
        font = pygame.font.SysFont("Chalkboard", 16)
        self.instruction_str = 'Use the arrow keys to move & Space bar to shoot'
        self.instruction_image = font.render(self.instruction_str, True, text_color)
        self.instruction_rect = self.instruction_image.get_rect()
        self.instruction_rect.centerx = self.screen_rect.centerx
        self.instruction_rect.y = float(self.screen_rect.height * .70)

    def prep_title_footer(self):
        text_color = (255, 255, 255)
        font = pygame.font.SysFont("Times New Roman", 14)
        self.footer_str = 'Version 1.0.0 Created by Robert L. Norwood'
        self.footer_image = font.render(self.footer_str, True, text_color)
        self.footer_rect = self.footer_image.get_rect()
        self.footer_rect.midbottom = self.screen_rect.midbottom


    def show_title(self):
        """Draws the title screen to the game screen"""
        self.screen.blit(self.game_logo, self.game_logo_rect)
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.sec_title_image, self.sec_title_rect)
        self.screen.blit(self.footer_image, self.footer_rect)
        self.screen.blit(self.instruction_image, self.instruction_rect)





