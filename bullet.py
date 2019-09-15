import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # A class to manage bullets fired from the ship

    def __init__(self, si_game):
        # Create a bullet object at the ship's current position
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = self.settings.bullet_color