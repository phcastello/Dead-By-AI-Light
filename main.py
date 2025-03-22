import pygame
import math
import random

from game.characters import *

# Configurações iniciais
FPS = 60

# Inicializa o Pygame
pygame.init()

# Configurações de tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dead By AI light")
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BCG_COLOR = (20,20,20)

# Criar o Killer e o Survivor com raio apropriado
killer = Killer(100, 100, 30, (255, 0, 0))
survivor = Survivor(300, 300, 20, (0, 0, 255))

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Captura teclas pressionadas
    keys = pygame.key.get_pressed()

    # Calcula o deslocamento do Killer
    killer_dx = keys[pygame.K_d] - keys[pygame.K_a]  # Direita - Esquerda
    killer_dy = keys[pygame.K_s] - keys[pygame.K_w]  # Baixo - Cima

    # Calcula o deslocamento do Survivor
    survivor_dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]  # Direita - Esquerda
    survivor_dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]  # Baixo - Cima

    # Movimento dos personagens
    killer.move(killer_dx, killer_dy)
    survivor.move(survivor_dx, survivor_dy)

    # Debug: Printa informações do Killer e do Survivor
    # print(f"Killer -> Pos: ({killer.rect.x}, {killer.rect.y}), Speed: {killer.speed}, "
    #       f"Radius: {killer.radius}, Direction: ({killer_dx}, {killer_dy})")
    # print(f"Survivor -> Pos: ({survivor.rect.x}, {survivor.rect.y}), Speed: {survivor.speed}, "
    #       f"Radius: {survivor.radius}, Direction: ({survivor_dx}, {survivor_dy})")

    # Renderização
    screen.fill(BCG_COLOR)  # Fundo branco
    all_sprites.draw(screen)  # Desenha os personagens na tela
    
    pygame.display.flip()  # Atualiza a tela

pygame.quit()
