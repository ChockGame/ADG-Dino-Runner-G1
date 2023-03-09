import random
import pygame
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.components.obstacles.bird import bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            cac = random.randint(0, 2)
            if cac == 0:
                self.obstacles.append(cactus())
            elif cac == 1:
                self.obstacles.append(cactus())
            elif cac == 2:
                self.obstacles.append(bird())

        for obstacle in self.obstacles:
                obstacle.update(game_speed, self.obstacles)
                if player.rect.colliderect(obstacle.rect):
                    pygame.time.delay(500)
                    on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []