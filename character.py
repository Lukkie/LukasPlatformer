import pygame

from bullet import Bullet


class Character:
    def __init__(self, screen, entities):
        self.screen = screen
        self.entities = entities

        # TODO: Dynamisch aanmaken?
        self.charHeight = 10
        self.charHorizon = screen.horizon - self.charHeight
        self.speed = 2
        self.charX, self.charY = (self.screen.width / 2, self.charHorizon)
        self.jumping = False
        self.jumpHeight = 200
        self.maxJumpIndex = 50
        self.jumpIndex = - self.maxJumpIndex  # Position in the jumping hyperbole
        self.rect = pygame.Rect(self.charX, self.charY, self.charHeight, self.charHeight)

        self.charcolor = (255, 255, 255)  # White

        # Shooting
        self.orientation = 1  # 1 if right, -1 if left
        self.firerate = 20  # how many frames to wait until next bullet
        self.fireindex = 0  # Will count to firerate until it can shoot again

    def move_right(self):
        self.charX = (self.charX + self.speed) % self.screen.width
        self.orientation = 1

    def move_left(self):
        self.charX = (self.charX - self.speed) % self.screen.width
        self.orientation = -1

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.jumpIndex = -self.maxJumpIndex

    def draw_char(self):
        self.rect = pygame.Rect(self.charX, self.charY, self.charHeight, self.charHeight)
        pygame.draw.rect(self.screen.surface, self.charcolor, self.rect)

    def shoot(self):
        if 0 < self.fireindex <= self.firerate:
            # Bullet is already shooting
            pass
        else:
            self.fireindex = 1
            # Create bullet and add to list in entities
            speed = 5
            size = 4
            bullet = Bullet(self.charX, self.charY + self.charHeight/2 - size/2,
                            self.orientation, speed, size, self.screen)
            self.entities.add_bullet(bullet)

    def update_activities(self):
        # Jumping
        if self.jumping:
            self.jumpIndex += 1

            a = self.jumpHeight / (self.maxJumpIndex ** 2)
            height = self.jumpHeight - a * (self.jumpIndex ** 2)
            self.charY = self.charHorizon - height

            if self.jumpIndex >= self.maxJumpIndex:
                self.jumping = False

        # Shooting
        if 0 < self.fireindex <= self.firerate:
            self.fireindex += 1
