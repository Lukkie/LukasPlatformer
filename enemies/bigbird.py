import pygame

from enemies.floater import Floater


class BigBird(Floater):
    """
    Generates a BigBird on a random location
    """
    def __init__(self, screen, char, sprites):
        size = 100
        super().__init__(screen, char, size)
        self.speed = 1
        self.health = 10
        self.sprite = pygame.transform.smoothscale(sprites.enemy_sprites["bigbird"], (size, size))
