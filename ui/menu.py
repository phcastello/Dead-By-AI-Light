import pygame
from ui import botao

pygame.init()

# Configurações da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu Principal")

# Variáveis de estado do jogo
game_paused = False  # Indica se o jogo está pausado
menu_state = "main"  # Estado atual do menu ("main" ou "options")

# Fonte e cores
font = pygame.font.SysFont("Courier", 30)  # Fonte usada para o texto
TEXT_COL = (0, 0, 0)  # Cor do texto

# Carregamento das imagens dos botões
# Cada botão tem uma imagem associada que será exibida na interface
start_img = pygame.image.load("./assets/ImagensMenu/start.png").convert_alpha()
menu_img = pygame.image.load("./assets/ImagensMenu/menu.png").convert_alpha()
pause_img = pygame.image.load("./assets/ImagensMenu/pause.png").convert_alpha()
back_img = pygame.image.load("./assets/ImagensMenu/back.png").convert_alpha()
quit_img = pygame.image.load("./assets/ImagensMenu/quit.png").convert_alpha()
option_img = pygame.image.load("./assets/ImagensMenu/options.png").convert_alpha()

# Criação de instâncias dos botões
# Cada botão é posicionado em coordenadas específicas
start_button = botao.Button(305, 125, start_img, 1)
menu_button = botao.Button(297, 250, menu_img, 1)
pause_button = botao.Button(336, 375, pause_img, 1)
back_button = botao.Button(310, 450, back_img, 1)
quit_button = botao.Button(300, 375, quit_img, 1)
option_menu_button = botao.Button(297, 250, option_img, 1)
option_pause_button = botao.Button(297, 400, option_img, 1)

def draw_text(text, font, text_col, x, y):
    """
    Renderiza texto na tela.
    - text: Texto a ser exibido.
    - font: Fonte usada para renderizar o texto.
    - text_col: Cor do texto.
    - x, y: Coordenadas onde o texto será exibido.
    """
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def show_menu(game_paused=False, menu_state="main"):
    """
    Exibe o menu principal ou de opções.
    - game_paused: Indica se o jogo está pausado.
    - menu_state: Estado atual do menu ("main" ou "options").
    """
    running = True
    while running:
        screen.fill((69, 144, 117))  # Cor de fundo do menu

        if menu_state == "main":
            # Exibe os botões do menu principal
            if start_button.draw(screen):  # Inicia o jogo
                return True
            if option_menu_button.draw(screen):  # Vai para o menu de opções
                menu_state = "options"
            if quit_button.draw(screen):  # Sai do jogo
                return False

        elif menu_state == "options":
            # Exibe os botões e texto do menu de opções
            draw_text("Você está na aba de opções", font, TEXT_COL, 200, 200)
            if back_button.draw(screen):  # Volta para o menu principal
                menu_state = "main"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fecha o jogo
                return False

        pygame.display.update()  # Atualiza a tela

if __name__ == "__main__":
    show_menu()
    pygame.quit()
    exit()