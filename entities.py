from enemy import Enemy
from random import randint


class Entities:
    def __init__(self):
        self.bullets = []
        self.enemies = []
        self.char = None  # Needs to be changed

        self.enemyrate = 150  # How many frames between enemies
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
                killed = bullet.check_collision(self.enemies)
                if killed:
                    self.bullets.remove(bullet)
                    self.enemies.remove(killed)
                    score += 1
            else:
                self.bullets.remove(bullet)
        return score

    def update_enemies(self):
        """

        :return: False if game over, True else
        """
        for enemy in self.enemies:
            alive = enemy.update_location()
            if alive:
                if enemy.check_collision(self.char):
                    print("Game Over")
                    return False
            else:
                self.enemies.remove(enemy)

        return True

    def update_entities(self):
        points = self.update_bullets()
        alive = self.update_enemies()
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

    def generate_enemies(self, screen):
        if self.enemyindex >= self.enemyrate:
            self.enemyindex = 0

            # Generate random enemy
            random_direction = randint(0, 1)  # 1 is to the right, 0 is left
            orientation = random_direction * 2 - 1
            size = randint(20, 100)
            y_loc = screen.horizon - size
            x_loc = screen.width * (1-random_direction) - random_direction*size
            # x_loc = 300
            speed = randint(1, 2)

            enemy = Enemy(x_loc, y_loc, orientation, speed, size, screen)
            self.add_enemy(enemy)
        else:
            self.enemyindex += 1