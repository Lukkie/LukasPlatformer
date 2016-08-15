import pygame


class Bullet:
    def __init__(self, x_loc, y_loc, orientation, speed, size, screen):
        self.x_loc = x_loc
        self.speed = speed
        self.y_loc = y_loc
        self.orientation = orientation
        self.screen = screen

        self.color = (255, 255, 255)
        self.size = size

        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

    def update_location(self):
        """
        :return: True if inside window, else False
        """
        self.x_loc += (self.orientation*self.speed)
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)
        if 0 <= self.x_loc < self.screen.width:
            return True
        return False

    def check_collision(self, enemies):
        # Can only kill 1 enemy for now
        for enemy in enemies:
            # if self.x_loc <= enemy.x_loc <= self.x_loc + self.size and \
            #                         self.y_loc <= enemy.y_loc <= self.y_loc + self.size:
            if self.rect.colliderect(enemy.rect):
                print("Enemy killed")
                return enemy
        return None

    def draw(self):
        pygame.draw.rect(self.screen.surface, self.color,
                         self.rect)
