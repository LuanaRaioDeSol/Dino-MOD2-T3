import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH  # (SCREEN_WIDTH = constante)


class PowerUp(Sprite):
    def __init__(self, image, type): #função do __init__: configurando os eventos e a tela
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)   
        self.rect.y = random.randint(125, 175)

        self.start_time = 0    # = 0 porque o jogo começa zerado
        self.duration = random.randint(5, 10) # random usado para fazer a contagem do tempo.

    def update(self, game_speed, power_ups):   #
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

#*  draw é uma a sequencia do update e gameloop*