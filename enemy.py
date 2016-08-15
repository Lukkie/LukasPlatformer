import pygame


class Enemy:
    def __init__(self, x_loc, y_loc, orientation, speed, size, screen):
        # TODO: Type van enemy, damage
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.speed = speed
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
        if self.x_loc + self.size >= 0 and self.x_loc < self.screen.width:
            return True
        return False

    def check_collision(self, char):
        # TODO: Collision met speler checken
        if self.rect.colliderect(char.rect):
            print("Player killed")
            return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen.surface, self.color,
                         self.rect)
