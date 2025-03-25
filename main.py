import pygame

from ui.menu import show_menu
from game.characters import *

FPS = 60  # Taxa de quadros por segundo

pygame.init()

# Full Screen
# info = pygame.display.Info()  # Obtém informações sobre a resolução do monitor
# WIDTH, HEIGHT = info.current_w, info.current_h
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)  # Modo fullscreen
# pygame.display.set_caption("Dead By AI light")
# clock = pygame.time.Clock()

# Configurações de tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead By AI light")
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BCG_COLOR = (100, 100, 100)  # Cor de fundo

# Criação dos personagens
killer = Killer(100, 100, (255, 0, 0), 30, 3.5)
survivor = Survivor(300, 300, (0, 0, 255), 20, 3)

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(killer, survivor)

# Exibe o menu antes de iniciar o jogo
if not show_menu():
    pygame.quit()
    exit()

# Loop principal do jogo
running = True
while running:
    clock.tick(FPS)  # Controla a taxa de quadros

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fecha o jogo
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Sai do jogo
                running = False
            elif event.key == pygame.K_SPACE:  # Modifica temporariamente a velocidade
                killer.change_speed_temp(1, 1, FPS)
                survivor.change_speed_temp(4, 0.5, FPS)

    # Captura teclas pressionadas
    keys = pygame.key.get_pressed()

    # Calcula o deslocamento do Killer
    killer_dx = keys[pygame.K_d] - keys[pygame.K_a]
    killer_dy = keys[pygame.K_s] - keys[pygame.K_w]

    # Calcula o deslocamento do Survivor
    survivor_dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    survivor_dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    # Aplica o movimento dos personagens
    killer.move(killer_dx, killer_dy)
    survivor.move(survivor_dx, survivor_dy)

    # Atualiza os personagens
    killer.update()
    survivor.update()

    # Renderização
    screen.fill(BCG_COLOR)  # Preenche o fundo
    all_sprites.draw(screen)  # Desenha os sprites
    
    pygame.display.flip()  # Atualiza a tela

pygame.quit()
