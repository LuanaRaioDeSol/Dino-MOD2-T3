import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
X_POS = 80
Y_POS = 300
Y_POS_DUCK = 340
JUMP_VEL = 8.5


class Dinosaur(Sprite):  #Funções que serão chamadas a baixo:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.setup_state()

    def setup_state(self): #iniciando o jogo do 0
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()   #=correr
        elif self.dino_jump:
            self.jump()  #=pular
        elif self.dino_duck:
            self.duck() #=abaixar

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 9: #mecanismo do dinossauro correndo
            self.step_index = 0  #mecanismo do dinossauro correndo
   

    def run(self):   #função: correr 
        self.image = RUN_IMG[self.type][self.step_index // 5] #RUM_IMG = É uma constante
        self.dino_rect = self.image.get_rect()       
        self.dino_rect.x = X_POS  #X_POS =É uma constante
        self.dino_rect.y = Y_POS  #Y_POS =É uma constante 
        self.step_index += 1      #Essa função está chamando as imagens de quando o dino corre. Usando as posições com o Y e X

    def jump(self):    #função: pular
        self.image = JUMP_IMG[self.type]  #Essa função chamou as imagens do dino pulando.
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8  #Cada vez que ele pula cada obstáculo, ele ganha mais ponto e aumenta a velocidade em 4X mais. 
  

        if self.jump_vel < -JUMP_VEL:  # JUMP_VEL = constante 
            self.dino_rect_y = Y_POS   #Y_POS = constante
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):   #função: abaixar
        self.image = DUCK_IMG[self.type][self.step_index // 5]  #//5 = aqui está falando da velocidade.
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):  #Aqui finalizou a parte introdutória do jogo
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
