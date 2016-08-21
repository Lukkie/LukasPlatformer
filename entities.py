from random import randint

from enemies.bigbird import BigBird
from enemies.enemy import Enemy
from enemies.fastjumper import FastJumper
from enemies.fastwalker import FastWalker
from enemies.fatwalker import FatWalker
from enemies.highjumper import HighJumper
from enemies.jumper import Jumper
from enemies.smallbird import SmallBird


class Entities:
    def __init__(self, difficulty):
        self.difficulty = difficulty  # By how much the max_speed of enemies per cycle

        self.bullets = []
        self.enemies = []
        self.char = None  # Needs to be changed

        self.enemyrate = 600  # How many frames between enemies
        self.enemyindex = 0

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def update_bullets(self):
        score = 0
        for bullet in self.bullets:
            alive = bullet.update_location()
            if alive:
                killed, hit = bullet.check_collision(self.enemies)
                if killed:
                    self.bullets.remove(bullet)
                    self.enemies.remove(killed)
                    score += 1
                elif hit:
                    self.bullets.remove(bullet)
            else:
                self.bullets.remove(bullet)
        return score

    def update_enemies(self):
        """
        :return: False if game over, True else
        """
        for enemy in self.enemies:
            enemy.update_location()
            if enemy.check_collision(self.char):
                print("Game Over")
                return False
        return True

    def update_entities(self):
        points = self.update_bullets()
        alive = self.update_enemies()
        self.enemyrate *= self.difficulty
        return alive, points

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw()

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.draw()

    def draw_entities(self):
        self.draw_bullets()
        self.draw_enemies()

    # def generate_enemies(self, screen):
    #     if self.enemyindex >= self.enemyrate:
    #         self.enemyindex = 0
    #
    #         # size = randint(20, 50)
    #         size = 20
    #         x_loc = screen.width - randint(0, 1)*(screen.width+size)
    #         y_loc = randint(size, screen.horizon-size)
    #         # speed = self.min_speed + (self.max_speed-self.min_speed)*random()
    #
    #         enemy = Enemy(x_loc, y_loc, screen, self.char)
    #         self.add_enemy(enemy)
    #         self.max_speed += self.difficulty
    #     else:
    #         self.enemyindex += 1

    def generate_enemies(self, screen, sprites):
        if self.enemyindex >= self.enemyrate:
            self.enemyindex = 0

            random_enemy = randint(0, 5)
            enemy = None
            if random_enemy == 0:
                enemy = FatWalker(screen, self.char, sprites)
            elif random_enemy == 1:
                enemy = SmallBird(screen, self.char, sprites)
            elif random_enemy == 2:
                enemy = HighJumper(screen, self.char, sprites)
            elif random_enemy == 3:
                enemy = FastJumper(screen, self.char, sprites)
            elif random_enemy == 4:
                enemy = BigBird(screen, self.char, sprites)
            elif random_enemy == 5:
                enemy = FastWalker(screen, self.char, sprites)

            self.add_enemy(enemy)
        else:
            self.enemyindex += 1
