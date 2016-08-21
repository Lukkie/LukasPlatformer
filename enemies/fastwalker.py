import pygame

from enemies.walker import Walker


class FastWalker(Walker):
    """
    Generates a FastWalker on a random location
    """
    def __init__(self, screen, char, sprites):
        size = 100
        super().__init__(screen, char, size)
        self.speed = 3
        self.health = 1
        self.sprite = pygame.transform.smoothscale(sprites.enemy_sprites["fastwalker"], (size, size))
