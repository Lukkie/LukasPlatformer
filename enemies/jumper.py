from random import randint

import pygame

from enemies.enemy import Enemy


class Jumper(Enemy):
    """
    Generates a jumping enemy on a random location, being left or right side of screen
    """
    def __init__(self, screen, char, size):
        super().__init__(screen, char)
        self.size = size
        self.y_loc = screen.horizon - self.size
        self.y_horizon = self.y_loc
        self.x_loc = screen.width - randint(0, 1) * (screen.width + self.size)
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

        self.jumpIndex = 0
        self.jumpHeight = 200
        self.maxJumpIndex = 30
        self.direction = 1 if self.char.rect.x > self.x_loc else -1

    def update_location(self):
        self.x_loc += self.speed * self.direction

        self.jumpIndex += 1
        if self.jumpIndex > self.maxJumpIndex:
            self.jumpIndex = -self.maxJumpIndex
            self.direction = 1 if self.char.rect.x > self.x_loc else -1

        a = self.jumpHeight / (self.maxJumpIndex ** 2)
        height = self.jumpHeight - a * (self.jumpIndex ** 2)
        self.y_loc = self.y_horizon - height

        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)
