import pygame


class Bullet:
    def __init__(self, x_loc, y_loc, x_speed, y_speed, size, screen):
        self.x_loc = x_loc
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.y_loc = y_loc
        self.screen = screen

        self.color = (255, 255, 255)
        self.size = size

        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

    def update_location(self):
        """
        :return: True if inside window, else False
        """
        self.x_loc += self.x_speed
        self.y_loc += self.y_speed
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

        # Still inside window?
        if self.rect.colliderect(self.screen.surface.get_rect()):
            return True
        return False

    def check_collision(self, enemies):
        # Can only kill 1 enemy for now
        for enemy in enemies:
            # if self.x_loc <= enemy.x_loc <= self.x_loc + self.size and \
            #                         self.y_loc <= enemy.y_loc <= self.y_loc + self.size:
            if self.rect.colliderect(enemy.rect):
                if enemy.hit_by_bullet():
                    print("Enemy has %s health left" % enemy.health)
                    return None, enemy
                else:
                    print("Enemy killed")
                    return enemy, enemy
        return None, None

    def draw(self):
        pygame.draw.rect(self.screen.surface, self.color,
                         self.rect)
