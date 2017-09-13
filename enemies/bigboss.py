import pygame

from enemies.walker import Walker


class BigBoss(Walker):
    """
    Generates a BigBoss on a random location
    """
    def __init__(self, screen, char, sprites):
        size = 300
        super().__init__(screen, char, size)
        self.speed = 0.25
        self.health = 75
        self.sprite = pygame.transform.smoothscale(sprites.enemy_sprites["bigboss"], (size, size))
        self.points = 20
