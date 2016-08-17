
class World:
    def __init__(self):
        # Image
        self.background = None

        # List of sprites (enemies, bullets, platforms)
        self.entities = None
        self.platforms = None

        # Shifting
        self.shift = 0  # Positive shift = move image to the right = walk to the left
        self.limit = 100000

        self.char = None
        self.screen = None

    def draw(self):
        blue = (0, 0, 50)
        self.screen.fill(blue)
        self.screen.surface.blit(self.background, (self.shift, 0))

    def shift_world(self, shift_x):
        self.shift += shift_x
        self.char.charX -= shift_x

        for bullet in self.entities.bullets:
            bullet.x_loc += shift_x

        for enemy in self.entities.enemies:
            enemy.x_loc += shift_x
