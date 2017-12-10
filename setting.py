class Settings:

    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1

        # bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 200
        self.bullet_height = 15
        self.bullet_color = 60, 60, 252
        self.bullet_allowed = 10
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 2

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale




