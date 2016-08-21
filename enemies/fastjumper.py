import pygame

from enemies.jumper import Jumper


class FastJumper(Jumper):
    """
    Generates a FastJumper on a random location
    """
    def __init__(self, screen, char, sprites):
        size = 70
        super().__init__(screen, char, size)
        self.jumpHeight = 200
        self.maxJumpIndex = 70
        self.speed = 1.5
        self.health = 1
        self.sprite = pygame.transform.smoothscale(sprites.enemy_sprites["fastjumper"], (size, size))
