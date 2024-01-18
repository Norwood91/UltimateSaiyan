import pygame.font
from pygame.sprite import Group
from hero_ship import Hero

class Scoreboard:
    """A class to report scoring information"""
    def __init__(self, ui_game):
        self.ui_game = ui_game
        self.screen = ui_game.game_screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ui_game.settings
        self.stats = ui_game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Times New Roman", 20)
        self.prep_score()
        self.prep_high_score()
        self.prep_game_level()
        self.prep_high_level()
        self.prep_hero_ships()

    def prep_score(self):
        """turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display score at top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.score_rect.top

    def prep_game_level(self):
        """Turn the level into a rendered image"""
        level_str = f"Level: {self.stats.game_level}"
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.score_rect.centerx
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_level(self):
        """Turn the high score into a rendered image"""
        high_level = self.stats.high_level
        high_level_str = "High Level: {:}".format(high_level)
        self.high_level_image = self.font.render(high_level_str, True, self.text_color)

        self.high_level_rect = self.high_level_image.get_rect()
        self.high_level_rect.right = self.screen_rect.right - 20
        self.high_level_rect.top = self.high_score_rect.bottom + 10

    def prep_hero_ships(self):
        """Show user how many ships(lives) they have left"""
        self.ships = Group()
        for ship_number in range(self.stats.hero_ships_left):
            ship = Hero(self.ui_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def check_high_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def check_high_level(self):
        """Check to see if there's a new high level"""
        if self.stats.game_level > self.stats.high_level:
            self.stats.high_level = self.stats.game_level
            self.prep_high_level()

    def show_score(self):
        """Draws the scores, level and the lives left to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_level_image, self.high_level_rect)
        self.ships.draw(self.screen)

