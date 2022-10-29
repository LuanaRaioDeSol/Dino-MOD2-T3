import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

  
    def execute(self):       #Chamei a função do self.running que tá no código base a cima, e coloquei no laço.
        self.running = True  #Enquanto o jogo estiver redando ok, se ele não rodar mais ele vai aparecer um menu 
        while self.running:  #(menu=pra apertar qualquer tecla e ele reeniciar o jogo, ou seja, não tem fim)
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()


    def run(self):                ##gameLoop = A BASE DO JOGO. 
        self.playing = True       ##Ele não está no código base, mas,  ele ajuda a chamar as funções que estão no código base.
        self.obstacle_manager.reset_obstacles() ##Ele existe pra o código não parar.
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()


 #detalhando o gameLoop
    def events(self):                     #Detalhando os events                
        for event in pygame.event.get():  #Usar o pygame pra criar os eventos e os seus tipos.
            if event.type == pygame.QUIT: #Uso das constantes, coforme for acontecendo os eventos fica nesse gameLoop. Ele pode sair, então:
                self.playing = False      #o jogador para de jogar
                self.running = False      #O jogo para de rodar 
   

    def update(self):                         #Detalhando o update
        user_input = pygame.key.get_pressed() #Usando o input pro próprio eupdate seguir a lógica conforme o jogo vai acontecendo. Pois não tenho como prever o desempenho do jogador. 
        self.player.update(user_input)        #Meu jogador vai dar um update corforme as coisas vão acontecendo.
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)


    
    def update_score(self):         #Criei uma função pra criar uma lógica da contagem de aumento da velocidade de acordo com a contagem de pontuação. 
        self.score += 1             #Aqui usei a lógica de conversão. #Lógica: quanto mais ponto ganhar, mais rápido fica.
        if self.score % 100 == 0:    #Se a pontuação aumentar, consequentemente, a velocidade vai aumentar em 5 cada vez que a pontução aumenta
           self.game_speed += 5

    def draw(self):          #COMEÇANDO A DESENHAR O QUE PRECISA TER NO JOGO:
        self.clock.tick(FPS)          #desenhando o relogio
        self.screen.fill(( 252 , 233 , 79 )) # "#FFFFFF"  #desenhando o fundo do jogo
        self.draw_background()      #background = O senário de fundo do jogo
        self.player.draw(self.screen)     #desenhando o jogador
        self.obstacle_manager.draw(self.screen) #desehando os obstáculos 
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)#Tem dois power pq tem dois senários. 1= senário do jogo. 2= senário de quando perde e tem a reeiniciação do jogo.
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):  #Desenhando o fundo do jogo:
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))    #self.screen= usado pra desenhar todos os lados do jogo.
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        #o que muda nesse background? conforme o jogo vai acontecendo eu vou pulando os obstáculos e, consequentemente, aumentando a velocidade.
 
    def draw_score(self):
         draw_message_component(  #draw_message_component = usado como input, pois não sei em que ponto as coisas irão aparecer
            f"Score: {self.score}  ",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50
        )   
  #Funções dos poderes:
    def draw_power_up_time(self): #desenhar  os poderes
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:  #programando a contagem do relogio. Se o meu tempo aparecer maior ou igual a 0, vai aparecer uma menssagem.
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,      #tamanho da fonte(Letras)  
                    pos_x_center = 500,  #onde vai ficar a mensagem no cenário do jogo. x= horizontal
                    pos_y_center = 40,  #onde vai ficar a mensagem no cenário do jogo. Y=  vertical
 
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():  #Nessa função estou lidando com os event on menu
            if event.type == pygame.QUIT: #no pygame de eventos se meu player der falso o jogo acaba. mas usamos o elif para ter a reeniciação automática.
                self.playing = False    
                self.running = False
            elif event.type == pygame.KEYDOWN:  
                self.run()   ##= ou o jogo acaba, ou ele reenicia.

        
    def show_menu(self):     #codificando o menu do jogo, ou seja, a abertura do jogo.
        self.screen.fill(( 237 , 212 , 0 )) #cor do fundo da aberturab do jogo.
        half_screen_height = SCREEN_HEIGHT // 2 # half_screen_height=
        half_screen_width = SCREEN_WIDTH // 2   # // =divisão inteira


        if self.death_count == 0:
           draw_message_component("Pressione qualquer tecla para iniciar", self.screen)
        else:
            draw_message_component("Você perdeu!!! ", self.screen, pos_y_center=half_screen_height + 100) ## +100 é a posição da frase na tela
            draw_message_component("Pressione qualquer tecla para reiniciar o jogo", self.screen, pos_y_center=half_screen_height + 160)
            draw_message_component(
                f"Your Score: {self.score} ",
                self.screen,
                pos_y_center=half_screen_height - 150
            )            
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 30))

        pygame.display.flip()

        self.handle_events_on_menu()
                