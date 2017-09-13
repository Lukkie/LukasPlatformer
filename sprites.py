import pygame
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Sprites:
    def __init__(self):
        self.player_walk_right = []
        self.player_walk_left = []
        self.player_jump_left = None
        self.player_jump_right = None
        self.player_idle = None

        self.enemy_sprites = {}

    def load_player_sprites(self, directory):
        self.load_walk_sprites('%s\\%s' % (directory, "walk"))
        self.load_idle_sprite('%s\\%s' % (directory, "idle"))
        self.load_jump_sprite('%s\\%s' % (directory, "jump"))

    def load_walk_sprites(self, directory):
        """
        Directory should contain PNGs
        :param directory:
        """
        for filename in os.listdir(resource_path(directory)):
            if filename.endswith(".png"):
                image = pygame.image.load('%s\\%s' % (resource_path(directory), filename)).convert_alpha()
                self.player_walk_right.append(image)
                self.player_walk_left.append(pygame.transform.flip(image.copy(), True, False))

    def load_idle_sprite(self, directory):
        filename = os.listdir(resource_path(directory))[0]
        assert filename.endswith(".png"), "File is not a PNG"
        image = pygame.image.load('%s\\%s' % (resource_path(directory), filename)).convert_alpha()
        self.player_idle = image

    def load_jump_sprite(self, directory):
        filename = os.listdir(resource_path(directory))[0]
        assert filename.endswith(".png"), "File is not a PNG"
        image = pygame.image.load('%s\\%s' % (resource_path(directory), filename)).convert_alpha()
        self.player_jump_right = image
        self.player_jump_left = pygame.transform.flip(image.copy(), True, False)

    def load_enemy_sprites(self, directory):
        for filename in os.listdir(resource_path(directory)):
            if filename.endswith(".png"):
                image = pygame.image.load('%s\\%s' % (resource_path(directory), filename)).convert_alpha()
                name = filename.replace(".png", "")
                self.enemy_sprites[name] = image
