class GameStats:
    """Track stats for the entire game"""

    def __init__(self, ui_game):
        self.settings = ui_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_level_file = 'high_level.txt'
        self.high_score_file = 'high_score.txt'
        with open(self.high_level_file, 'r') as file:
            contents = file.read()
            self.high_level = int(contents)
        with open(self.high_score_file, 'r') as file:
            contents = file.read()
            self.high_score = int(contents)

    def reset_stats(self):
        """Initalizes stats that can change during the game"""
        self.hero_ships_left = self.settings.hero_ship_limit
        self.game_active = True
        self.score = 0
        self.game_level = 1
