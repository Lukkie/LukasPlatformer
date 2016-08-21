
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

        if shift_x > 0:
            self.char.move_left_animation()
        else:
            self.char.move_right_animation()

        for bullet in self.entities.bullets:
            bullet.x_loc += shift_x

        for enemy in self.entities.enemies:
            enemy.x_loc += shift_x
