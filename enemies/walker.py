from random import randint

import pygame

from enemies.enemy import Enemy


class Walker(Enemy):
    """
    Generates a walking enemy on a random location, being left or right side of screen
    """
    def __init__(self, screen, char, size):
        super().__init__(screen, char)
        self.size = size
        self.y_loc = screen.horizon - self.size
        self.x_loc = screen.width - randint(0, 1) * (screen.width + self.size)
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

    def update_location(self):
        if self.char.rect.x < self.x_loc:
            self.x_loc -= self.speed
        else:
            self.x_loc += self.speed
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)
