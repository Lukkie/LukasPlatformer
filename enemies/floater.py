from random import randint

import pygame
import math

from enemies.enemy import Enemy


class Floater(Enemy):
    """
    Generates a flying enemy on a random location,
    being left or right side of screen, at a random height
    """
    def __init__(self, screen, char, size):
        super().__init__(screen, char)
        self.size = size
        self.x_loc = screen.width - randint(0, 1)*(screen.width+size)
        self.y_loc = randint(size, screen.horizon-size)
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

    def update_location(self):
        # Calculate relative x and y speed
        x_diff = self.char.rect.x - self.x_loc  # TODO: use rect.x or charX?
        y_diff = self.char.rect.y - self.y_loc
        alpha = math.atan2(y_diff, x_diff)
        x_speed = math.cos(alpha) * self.speed
        y_speed = math.sin(alpha) * self.speed

        self.x_loc += x_speed
        self.y_loc += y_speed
        if self.y_loc >= self.screen.horizon - self.size:
            self.y_loc = self.screen.horizon - self.size  # Slide on floor if reaching horizon
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)
