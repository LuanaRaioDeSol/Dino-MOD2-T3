import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game): 
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:     # if = laço          
            self.obstacles.append(obstacle_type[random.randint(0,1)])  #
            
        for obstacle in self.obstacles:       #rodar os obstáculos aleatóriamente
            obstacle.update(game.game_speed, self.obstacles)  #função update: foi usada para criar os obstáculos...
            if game.player.dino_rect.colliderect(obstacle.rect): 
                if not game.player.has_power_up: #LAÇO dentro do for: CRIADO PRA APARECER UM OBSTÁCULO DE CADA VEZ.
                    pygame.time.delay(500)                       #o LAÇO só acontece se ouver uma ação do FOR.
                    game.playing = False
                    game.death_count += 1
                    break    #USADO PARA: após colisão, remover os obstáculos e reeniciar o jogo.
                else:
                    self.obstacles.remove(obstacle)

    def reset_obstacles(self):   
        self.obstacles = []         

    def draw(self, screen):      #ultima função: draw = redesenhando conforme o desenvolvimento imprevisível do jogo.
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            