import pygame


class Enemy(object):
    def __init__(self, screen, char):
        # Following attributes should be assigned by subclasses
        self.speed = 2
        self.health = 1
        self.size = 20
        self.sprite = None
        self.x_loc = 0
        self.y_loc = screen.horizon - self.size
        # Possible extensions: Damage (not instakill), shooting, ..
        #######################################################

        self.screen = screen
        self.char = char

        self.color = (255, 255, 255)

        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

    def update_location(self):
        print("TODO: Implement update_location")
        pass

    def check_collision(self, char):
        if self.rect.colliderect(char.rect):
            print("Player killed")
            return True
        return False

    def draw(self):
        # pygame.draw.rect(self.screen.surface, self.color,
        #                  self.rect)
        self.screen.surface.blit(self.sprite, self.rect)

    def hit_by_bullet(self):
        """
        Enemy is hit by a bullet
        :return: Return True if enemy still alive, else False
        """
        self.health -= 1
        return True if self.health > 0 else False
