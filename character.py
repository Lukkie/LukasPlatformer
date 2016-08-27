import pygame

from bullet import Bullet
import math


class Character:
    def __init__(self, screen, entities, sprites):
        self.screen = screen
        self.entities = entities

        # Sprites
        self.sprites = sprites
        self.charHeight = self.sprites.player_walk_right[0].get_height()
        self.charWidth = self.sprites.player_walk_right[0].get_width()
        self.move_state = "I"  # I = Idle, L = Left, R = Right
        self.walk_index = 0  # Changes sprite every couple of frames to simulate walking
        self.walk_frames_per_change = 5
        self.walk_max_index = len(self.sprites.player_walk_right) * self.walk_frames_per_change

        # TODO: Dynamisch aanmaken? --> Uit input file lezen
        self.charHorizon = screen.horizon - self.charHeight
        self.speed = 2
        self.charX, self.charY = (self.screen.width / 2, self.charHorizon)  # Coordinates in world
        self.jumping = False  # True if jumping, else False
        self.jumpHeight = 200
        self.maxJumpIndex = 50
        self.jumpIndex = - self.maxJumpIndex  # Position in the jumping hyperbole
        # self.rect = pygame.Rect(self.charX, self.charY, self.charHeight, self.charHeight)
        self.rect = pygame.Rect(self.charX, self.charY, self.charWidth, self.charHeight)

        self.charcolor = (255, 255, 255)  # White

        # Shooting
        self.bullet_speed = 5
        self.firerate = 20  # how many frames to wait until next bullet
        self.fireindex = 0  # Will count to firerate until it can shoot again

        # Sound
        pygame.mixer.pre_init(22050, -16, 2, 128)
        pygame.init()
        pygame.mixer.quit()
        pygame.mixer.init(22050, -16, 2, 128)
        self.gun_sound = pygame.mixer.Sound(r'sounds\M4A1_Single-Kibblesbob-8540445.wav')
        self.gun_sound.set_volume(0.25)

    def move_right(self):
        self.move(self.speed)
        self.move_right_animation()

    def move_left(self):
        self.move(-self.speed)
        self.move_left_animation()

    def move_left_animation(self):
        self.move_state = "L"
        self.walk_index = (self.walk_index + 1) % self.walk_max_index

    def move_right_animation(self):
        self.move_state = "R"
        self.walk_index = (self.walk_index + 1) % self.walk_max_index

    def move(self, amount):
        self.charX = (self.charX + amount)
        self.rect.x = (self.rect.x + amount)

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.jumpIndex = -self.maxJumpIndex

    def draw_char(self):
        if self.move_state == "I":
            used_sprite = self.sprites.player_idle
        elif self.move_state == "L":
            if self.jumping:
                used_sprite = self.sprites.player_jump_left
            else:
                used_sprite = self.sprites.player_walk_left[self.walk_index //
                                                            self.walk_frames_per_change]
        else:  # Walking right
            if self.jumping:
                used_sprite = self.sprites.player_jump_right
            else:
                used_sprite = self.sprites.player_walk_right[self.walk_index //
                                                             self.walk_frames_per_change]

        self.screen.surface.blit(used_sprite, self.rect)
        # pygame.draw.rect(self.screen.surface, self.charcolor, self.rect)

    def shoot(self, target_x, target_y):
        if 0 < self.fireindex <= self.firerate:
            # Bullet is already shooting
            pass
        else:
            # Play sound
            self.gun_sound.stop()
            self.gun_sound.play()

            # Restart cooldown for shots
            self.fireindex = 1

            # Calculate relative x and y speed
            x_diff = target_x - self.rect.centerx
            y_diff = target_y - self.rect.centery
            alpha = math.atan2(y_diff, x_diff)
            x_speed = math.cos(alpha) * self.bullet_speed
            y_speed = math.sin(alpha) * self.bullet_speed

            # Create bullet and add to list in entities
            size = 4
            bullet = Bullet(self.rect.centerx, self.rect.y + self.charHeight/2 - size/2,
                            x_speed, y_speed, size, self.screen)
            self.entities.add_bullet(bullet)

    def update_activities(self):
        self.move_state = "I"  # Is called before checking movement left or right

        # Jumping
        if self.jumping:
            self.jumpIndex += 1

            a = self.jumpHeight / (self.maxJumpIndex ** 2)
            height = self.jumpHeight - a * (self.jumpIndex ** 2)
            self.charY = self.charHorizon - height
            self.rect.y = self.charHorizon - height

            if self.jumpIndex >= self.maxJumpIndex:
                self.jumping = False

        # Shooting
        if 0 < self.fireindex <= self.firerate:
            self.fireindex += 1
