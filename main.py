import pygame
import math
import random

from game.characters import *

# Configurações iniciais
FPS = 60

# Inicializa o Pygame
pygame.init()

# Configurações de tela


# Cria a janela em modo fullscreen
#screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
#info = pygame.display.Info()  # Obtém informações sobre a resolução do monitor
#WIDTH, HEIGHT = info.current_w, info.current_h
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead By AI light")
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Criar o Killer e o Survivor com raio apropriado
# TODO: Adicionar Spawn aleatório com margem de segurança do killer
killer = Killer(100, 100, (255, 0, 0), 30, 3.5)
survivor = Survivor(300, 300, (0, 0, 255), 20, 3)

all_sprites = pygame.sprite.Group()
all_sprites.add(killer, survivor)

# Loop Principal do Jogo
running = True
while running:
    clock.tick(FPS)
    
    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Adicionar opção para sair com a tecla ESC
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Captura teclas pressionadas
    keys = pygame.key.get_pressed()

    # Movimento dos personagens (usando normalização)
    killer.move(keys, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
    survivor.move(keys, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT)

    # Renderização
    screen.fill(WHITE)  # Fundo branco
    all_sprites.draw(screen)  # Desenha os personagens na tela
    
    pygame.display.flip()  # Atualiza a tela

pygame.quit()
