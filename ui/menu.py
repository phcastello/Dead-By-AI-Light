import pygame
from ui import botao

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
start_img = pygame.image.load("/home/phcastello/Documentos/Dead_By_AI_light/ui/ImagensMenu/start.png").convert_alpha()
menu_img = pygame.image.load("/home/phcastello/Documentos/Dead_By_AI_light/ui/ImagensMenu/menu.png").convert_alpha()
pause_img = pygame.image.load("/home/phcastello/Documentos/Dead_By_AI_light/ui/ImagensMenu/pause.png").convert_alpha()
back_img = pygame.image.load("/home/phcastello/Documentos/Dead_By_AI_light/ui/ImagensMenu/back.png").convert_alpha()
quit_img = pygame.image.load("/home/phcastello/Documentos/Dead_By_AI_light/ui/ImagensMenu/quit.png").convert_alpha()
option_img = pygame.image.load("/home/phcastello/Documentos/Dead_By_AI_light/ui/ImagensMenu/options.png").convert_alpha()

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

def show_menu(game_paused = False, menu_state = "main"):
    #Loop do jogo
    menu_state = "main"
    running = True

    while running:
        screen.fill((69, 144, 117))

        if menu_state == "main":
            if start_button.draw(screen):  # Se clicar em Start
                return True
            if option_menu_button.draw(screen):  # Se clicar em Options
                menu_state = "options"
            if quit_button.draw(screen):  # Se clicar em Quit
                return False

        elif menu_state == "options":
            # Exibir texto na tela
            draw_text("Você está na aba de opções", font, TEXT_COL, 200, 200)
            if back_button.draw(screen):  # Voltar ao menu principal
                menu_state = "main"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()

if __name__ == "__main__":
    show_menu()
    pygame.quit()
    exit()