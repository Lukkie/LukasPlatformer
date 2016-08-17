import os

import pygame


class Sprites:
    def __init__(self):
        self.player_walk_right = []
        self.player_walk_left = []
        self.player_jump_left = None
        self.player_jump_right = None
        self.player_idle = None

    def load_sprites(self, directory):
        self.load_walk_sprites('%s\\%s' % (directory, "walk"))
        self.load_idle_sprite('%s\\%s' % (directory, "idle"))
        self.load_jump_sprite('%s\\%s' % (directory, "jump"))

    def load_walk_sprites(self, directory):
        """
        Directory should contain PNGs
        :param directory:
        """
        for filename in os.listdir(directory):
            if filename.endswith(".png"):
                image = pygame.image.load('%s\\%s' % (directory, filename)).convert_alpha()
                self.player_walk_right.append(image)
                self.player_walk_left.append(pygame.transform.flip(image.copy(), True, False))

    def load_idle_sprite(self, directory):
        filename = os.listdir(directory)[0]
        assert filename.endswith(".png"), "File is not a PNG"
        image = pygame.image.load('%s\\%s' % (directory, filename)).convert_alpha()
        self.player_idle = image

    def load_jump_sprite(self, directory):
        filename = os.listdir(directory)[0]
        assert filename.endswith(".png"), "File is not a PNG"
        image = pygame.image.load('%s\\%s' % (directory, filename)).convert_alpha()
        self.player_jump_right = image
        self.player_jump_left = pygame.transform.flip(image.copy(), True, False)