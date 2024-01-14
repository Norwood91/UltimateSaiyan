
class GameStats:
    """Track stats for the entire game"""
    def __init__(self, ui_game):
        self.settings = ui_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initalizes stats that can change during the game"""
        self.hero_ships_left = self.settings.hero_ship_limit
        self.game_active = True