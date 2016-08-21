import pygame

from enemies.walker import Walker


class FatWalker(Walker):
    """
    Generates a FatWalker on a random location
    """
    def __init__(self, screen, char, sprites):
        size = 100
        super().__init__(screen, char, size)
        self.speed = 0.5
        self.health = 20
        self.sprite = pygame.transform.smoothscale(sprites.enemy_sprites["fatwalker"], (size, size))
