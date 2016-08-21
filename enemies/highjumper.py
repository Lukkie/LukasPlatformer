import pygame

from enemies.jumper import Jumper


class HighJumper(Jumper):
    """
    Generates a HighJumper on a random location
    """
    def __init__(self, screen, char, sprites):
        size = 100
        super().__init__(screen, char, size)
        self.jumpHeight = 400
        self.maxJumpIndex = 100
        self.speed = 0.7
        self.health = 1
        self.sprite = pygame.transform.smoothscale(sprites.enemy_sprites["highjumper"], (size, size))
