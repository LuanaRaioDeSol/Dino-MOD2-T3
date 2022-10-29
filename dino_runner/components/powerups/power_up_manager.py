import random
import pygame

from dino_runner.components.powerups.shield import Shield


class PowerUpManager:
    def __init__(self): #Função: dos poderes, e quando eles irão aparecer!
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score: #configurando quando que vai aparecer os poderes e a pontuação. Se os poderes, e, quando ele vão aprecer é igual a pontuação.
            self.when_appears += random.randint(200, 300)     # random= posições aleatórias dos objetos.   (200, 300)= configurção do scord
            self.power_ups.append(Shield())   #chamando a função pro Shield.

    def update(self, score, game_speed, player): 
        self.generate_power_up(score)
        for power_up in self.power_ups: #um laço dentro de outro laço, ou seja, só acontece o segundo laço se o primeiro laço acontecer.
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect): #colisão
                power_up.start_time = pygame.time.get_ticks() #inicialisação
                player.shield = True     
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000) 
                self.power_ups.remove(power_up)

    def draw(self, screen):     #O ultimo do gameloop.
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)