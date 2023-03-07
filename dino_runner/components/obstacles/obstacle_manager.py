import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager():
    def __init__(self):
        self.obstacles =[]

    def update(self, game_speed, player, game, screen):
        if not self.obstacles:
            self.obstacles.append(Cactus())

        if len(self.obstacles) == 0:        
            if random.randint(0, 2) == 0:
                self.obstacles.remove(SMALL_CACTUS)             
            elif random.randint(0, 2) == 1:                         #**** variables de cambio de imagen ( intercalacion ) *****
                self.obstacles.remove(LARGE_CACTUS)
            elif random.randint(0, 2) == 2:
                self.obstacles.remove(BIRD)
            
        for obstacle in self.obstacles:
                obstacle.update(game_speed, self.obstacles)
                if player.dino_rect.collidarect(obstacle.rect):
                    pygame.time.delay(500)
                    game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)