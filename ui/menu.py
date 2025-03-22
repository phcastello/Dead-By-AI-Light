import pygame
import botao

pygame.init()

#Tamanho da janela/nn precisa levar pro projeto final
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Nome da aba
pygame.display.set_caption("Menu Principal")

#Variaveis de jogo
game_paused = False
menu_state= "main"

#Fonte 
font = pygame.font.SysFont("Courier", 30)

#Cor do texto
TEXT_COL = (0,0,0)

#Load nas imagens dos botoes
start_img = pygame.image.load("ImagensMenu/start.png").convert_alpha()
menu_img = pygame.image.load("ImagensMenu/menu.png").convert_alpha()
pause_img = pygame.image.load("ImagensMenu/pause.png").convert_alpha()
back_img = pygame.image.load("ImagensMenu/back.png").convert_alpha()
quit_img = pygame.image.load("ImagensMenu/quit.png").convert_alpha()
option_img = pygame.image.load("ImagensMenu/options.png").convert_alpha()

#criar instancia dos botoes
start_button = botao.Button(305, 125, start_img, 1)
menu_button = botao.Button(297, 250, menu_img, 1)
pause_button = botao.Button (336, 375, pause_img, 1)
back_button = botao.Button (310, 450, back_img, 1)
quit_button = botao.Button (300, 375, quit_img, 1)
option_menu_button = botao.Button (297,250, option_img, 1)
option_pause_button = botao.Button (297, 400, option_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render (text, True, text_col)
    screen.blit (img, (x,y))

#Loop do jogo
run = True
while run:

    #Cor do menu
    screen.fill ((69, 144, 117))

    #Checar se o jogo está pausado
    if game_paused == False:
        if menu_state == "main":
            if start_button.draw(screen):
                game_paused = True
            if option_menu_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        if menu_state == "options":
            if back_button.draw(screen):
                menu_state = "main"

    #Quando acontecer algum evento
    if game_paused == True:
        #Texto, Fonte, Cor, Posição X, Posição Y
        draw_text ("Pressione ESC para pausar", font, TEXT_COL, 160, 250)
        if option_pause_button.draw(screen):
                menu_state = "options"
        if menu_state == "options":
            if back_button.draw(screen):
                menu_state = "main"
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #Keydown = uma tecla foi pressionada
            if event.key == pygame.K_ESCAPE: #pygame.K_(Qualquer tecla)
                print ("Esc")
                game_paused = not game_paused

        #Apertar o X da janela
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()