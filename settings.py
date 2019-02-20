import random


class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 100)

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100, 0, 0)
        self.bullets_allowed = 5

        # used to spread out bullets fired at the same time
        self.bullet_spacer = 15

        self.fleet_drop_speed = 10

        self.ship_limit = 3

        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.alien_points = 10

        self.initialize_dynamic_settings()
        self.increase_speed()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 5
        self.ufo_speed = random.randint(3, 8)
        self.bullet_speed_factor = 7
        self.alien_speed_factor = 3
        self.fleet_direction = 1


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
