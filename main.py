import os
import pygame
import sys

from character import Character
from screen import Screen

from entities import Entities
from sprites import Sprites
from world import World

white = (255, 255, 255)
black = (0, 0, 0)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# TODO: * Bullet sprite + effect when enemy killed
# TODO: * Sound effects
# TODO: * Weapon pick-ups with higher firerate, bigger bullets, more damage
class App:
    def __init__(self):
        self.clock = None
        self._running = True
        self.fps = 150
        self.alive = True
        self.difficulty = 0.9999  # ]0, 1] Higher is easier

        # Sprites
        self.sprites = None

        # Entitites
        self.entities = None

        # Screen
        self.screen = None

        # Character
        self.char = None

        # World
        self.world = None
        self.buffer = 300

        # Stats
        self.playtime = 0.0
        self.lastboss = 0.0
        self.score = 0

        # Mouse
        self.mouseX, self.mouseY = (0, 0)

    def on_init(self):
        pygame.init()
        self._running = True

        # Screen
        self.screen = Screen()

        # Sprites
        self.sprites = Sprites()
        self.sprites.load_player_sprites(r'sprites\player\p1')
        self.sprites.load_enemy_sprites(r'sprites\enemy')

        # Entitites
        self.entities = Entities(self.difficulty)

        # Character
        self.char = Character(self.screen, self.entities, self.sprites)
        self.entities.char = self.char

        # World
        self.world = World()
        self.world.background = pygame.image.load(resource_path(r'backgrounds\Background1.png')).convert_alpha()
        self.world.screen = self.screen
        self.world.entities = self.entities
        self.world.limit = 3200
        self.world.char = self.char

        # Clock
        self.clock = pygame.time.Clock()

        # Mouse
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEMOTION:
            self.mouseX, self.mouseY = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_ESCAPE:
                self._running = False
            # Debug and testing
            if key == pygame.K_SPACE:
                print("Char: (%s, %s) - Rect: (%s, %s)" %
                      (self.char.charX, self.char.charY, self.char.rect.x, self.char.rect.y))
            if not self.alive:
                if key == pygame.K_RETURN or key == pygame.K_SPACE:
                    self.restart_game()

    def on_loop(self):
        if self.alive:
            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds

            # Key detection
            pressed = pygame.key.get_pressed()

            # Update activities
            self.char.update_activities()
            self.alive, points = self.entities.update_entities()
            self.score += points

            # Generate enemies
            self.entities.generate_enemies(self.screen, self.sprites)

            # Every 30 sec, generate a boss
            if self.lastboss + 30000.0 < self.playtime:
                self.lastboss = self.playtime
                self.entities.generate_boss(self.screen, self.sprites)

            # Movement
            # Left - Right
            left_pressed = pressed[pygame.K_LEFT] or pressed[pygame.K_a]
            right_pressed = pressed[pygame.K_RIGHT] or pressed[pygame.K_d]
            if left_pressed and not right_pressed:
                self.move_left()
            elif right_pressed and not left_pressed:
                self.move_right()
            # Jumping
            if pressed[pygame.K_UP] or pressed[pygame.K_w]:
                self.char.jump()

            # Shooting
            if pygame.mouse.get_pressed()[0]:
                self.char.shoot(self.mouseX, self.mouseY)

    def move_left(self):
        if self.char.charX - self.char.speed <= self.buffer:  # At start of world bound
            pass  # do nothing
        elif self.char.rect.x <= self.buffer:  # At buffer bound
            self.world.shift_world(self.char.speed)
        else:
            self.char.move_left()

    def move_right(self):

        if self.char.charX + self.char.speed >= self.world.limit - self.buffer:  # At start of world bound
            pass  # do nothing
        elif self.char.rect.x >= self.screen.width - self.buffer:  # At buffer bound
            self.world.shift_world(-self.char.speed)
        else:
            self.char.move_right()

    def on_render(self):
        self.screen.fill(black)

        if self.alive:
            # Draw world
            self.world.draw()

            # Draw character
            self.char.draw_char()

            # Draw entities
            self.entities.draw_entities()

        else:  # Game over
            font1 = pygame.font.SysFont("monospace", 100)
            label1 = font1.render("GAME OVER", 1, white)
            textpos1 = label1.get_rect()
            textpos1.centerx = self.screen.surface.get_rect().centerx
            textpos1.centery = self.screen.surface.get_rect().centery
            self.screen.surface.blit(label1, textpos1)

            font2 = pygame.font.SysFont("monospace", 20)
            label2 = font2.render("Press ENTER or SPACE to restart", 1, white)
            textpos2 = label2.get_rect()
            textpos2.centerx = self.screen.surface.get_rect().centerx
            textpos2.centery = textpos1.centery + textpos1.height
            self.screen.surface.blit(label2, textpos2)

        # Draw stats
        self.draw_score()

        # Update the screen
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def draw_score(self):
        myfont = pygame.font.SysFont("monospace", 20)
        label = myfont.render("Score: %s" % self.score, 1, white)
        textpos = label.get_rect()
        textpos.topleft = (20, 20)
        self.screen.surface.blit(label, textpos)
        diff_label = myfont.render("Difficulty: %s enemies/sec" %
                                   round(self.fps / self.entities.enemyrate, 2), 1, white)
        diff_textpos = label.get_rect()
        diff_textpos.topright = (self.screen.width - 250, 20)
        self.screen.surface.blit(diff_label, diff_textpos)

    def restart_game(self):
        self.alive = True
        self.score = 0
        self.playtime = 0
        self.on_init()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
