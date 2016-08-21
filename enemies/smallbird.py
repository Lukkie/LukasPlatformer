import pygame

from enemies.floater import Floater


class SmallBird(Floater):
    """
    Generates a SmallBird on a random location
    """
    def __init__(self, screen, char, sprites):
        size = 50
        super().__init__(screen, char, size)
        self.speed = 1
        self.health = 1
        self.sprite = pygame.transform.smoothscale(sprites.enemy_sprites["smallbird"], (size, size))
