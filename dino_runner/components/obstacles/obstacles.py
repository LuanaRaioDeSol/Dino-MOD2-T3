import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):  #desenvolvendo as imagens do obstáculos...
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() #essa função tem um efeito, que atravéns das ações do dino, ele redimensiona a imagem, ou seja, ela se adapta.
        self.rect.x = SCREEN_WIDTH  # = contante. 

    def update(self, game_speed, obstacles):  
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:  #chamando os obstáculos... pra ficar infinito, basicamente.
            obstacles.pop()

    def draw(self, screen):   # draw = refazer
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
        #finalizou os obstáculos...
        #*sempre que estiver um número negativo, está chamando um aposição*



        