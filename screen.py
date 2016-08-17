import pygame


# TODO: World class apart maken?
class Screen:
    def __init__(self):
        # TODO: Dynamisch aanmaken?
        self.surface = None
        self.size = self.width, self.height = 640, 512
        self.horizon = self.height - 64

        self.floorcolor = (255, 255, 255)  # white

        # Display
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Lukas Platformer')

    def fill(self, color):
        self.surface.fill(color)

    def draw_floor(self):
        pygame.draw.rect(self.surface, self.floorcolor,
                         pygame.Rect(0, self.height - 50, self.width, 50))
