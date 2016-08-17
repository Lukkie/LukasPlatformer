import pygame
import math

class Enemy:
    def __init__(self, x_loc, y_loc, speed, size, screen, char):
        # TODO: Type van enemy, damage
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.speed = speed
        self.screen = screen
        self.char = char

        self.color = (255, 255, 255)
        self.size = size

        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

    def update_location(self):
        # Calculate relative x and y speed
        x_diff = self.char.rect.x - self.x_loc
        y_diff = self.char.rect.y - self.y_loc
        alpha = math.atan2(y_diff, x_diff)
        x_speed = math.cos(alpha) * self.speed
        y_speed = math.sin(alpha) * self.speed

        self.x_loc += x_speed
        self.y_loc += y_speed
        if self.y_loc >= self.screen.horizon - self.size:
            self.y_loc = self.screen.horizon - self.size  # Slide on floor if reaching horizon
        self.rect = pygame.Rect(self.x_loc, self.y_loc, self.size, self.size)

    def check_collision(self, char):
        if self.rect.colliderect(char.rect):
            print("Player killed")
            return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen.surface, self.color,
                         self.rect)
