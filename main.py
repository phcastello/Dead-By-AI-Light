import pygame

from ui.menu import show_menu
from game.characters import *
from ui.menu import screen
from ui.menu import SCREEN_HEIGHT
from ui.menu import SCREEN_WIDTH

FPS = 60  # Taxa de quadros por segundo

pygame.init()

# Full Screen
# info = pygame.display.Info()  # Obtém informações sobre a resolução do monitor
# WIDTH, HEIGHT = info.current_w, info.current_h
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)  # Modo fullscreen
# pygame.display.set_caption("Dead By AI light")
# clock = pygame.time.Clock()

# Configurações de tela
#SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dead By AI light")
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BCG_COLOR = (100, 100, 100)  # Cor de fundo

#Lista de paredes
walls = [
    pygame.Rect(200, 150, 400, 4),  #wall2
    pygame.Rect(100, 300, 4, 200),  #wall1
    pygame.Rect(0, 0, SCREEN_WIDTH, 10),  #Upper wall
    pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10),  #Lower wall
    pygame.Rect(0, 0, 10, SCREEN_HEIGHT),  #Left wall
    pygame.Rect(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT), #Right wall
    pygame.Rect(200, 150, 300, 4),  
    pygame.Rect(400, 300, 4, 200),  
    pygame.Rect(100, 450, 235, 4),  
    pygame.Rect(600, 100, 4, 250),
    pygame.Rect(300, 74, 200, 4),
    pygame.Rect(400, 500, 250, 4) 
]


# Criação dos personagens
killer = Killer(100, 100, (255, 0, 0), 20, 3.2)
survivor = Survivor(300, 300, (0, 0, 255), 10, 3)

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(killer, survivor)

# Exibe o menu antes de iniciar o jogo
if not show_menu(screen):
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
            if event.key == pygame.K_SPACE:
                killer.change_speed_temp(1, 1, FPS)
                survivor.change_speed_temp(4, 0.5, FPS)
            attacked = killer.attack(survivor)
            if attacked:
                print("Sobrevivente atingido!")
            else:
                print("Errou o ataque.")


    # Captura teclas pressionadas
    keys = pygame.key.get_pressed()

    # Calcula o deslocamento do Killer
    killer_dx = keys[pygame.K_d] - keys[pygame.K_a]
    killer_dy = keys[pygame.K_s] - keys[pygame.K_w]

    # Calcula o deslocamento do Survivor
    survivor_dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    survivor_dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    # Aplica o movimento dos personagens
    new_killer = killer.rect.move(killer_dx * killer.speed, killer_dy * killer.speed)
    new_survivor = survivor.rect.move(survivor_dx * survivor.speed, survivor_dy * survivor.speed)

    new_killer_x = killer.rect.move(killer_dx * killer.speed, 0)
    new_survivor_x = survivor.rect.move(survivor_dx * survivor.speed, 0)

    if not any(new_killer_x.colliderect(wall) for wall in walls):
        killer.move(killer_dx, 0)  # Move apenas na horizontal

    if not any(new_survivor_x.colliderect(wall) for wall in walls):
        survivor.move(survivor_dx, 0)  # Move apenas na horizontal

    # Testa movimento vertical (cima/baixo)
    new_killer_y = killer.rect.move(0, killer_dy * killer.speed)
    new_survivor_y = survivor.rect.move(0, survivor_dy * survivor.speed)

    if not any(new_killer_y.colliderect(wall) for wall in walls):
        killer.move(0, killer_dy)  # Move apenas na vertical

    if not any(new_survivor_y.colliderect(wall) for wall in walls):
        survivor.move(0, survivor_dy)  # Move apenas na vertical

    current_time = pygame.time.get_ticks()
    killer.attack(survivor)

    # Atualiza os personagens
    killer.update()
    survivor.update()

    # Renderização
    screen.fill(BCG_COLOR)  # Preenche o fundo
    all_sprites.draw(screen)  # Desenha os sprites

    # Desenha a espada se estiver atacando
    if killer.show_sword:
        sword_rotated = pygame.transform.rotate(killer.sword_img, -45)  # ou outro ângulo se quiser girar
        sword_rect = sword_rotated.get_rect(center=(killer.x + 40, killer.y + 5))   # posição à frente do killer
        screen.blit(sword_rotated, sword_rect)

    
    for wall in walls:          #Desenha as paredes
        pygame.draw.rect(screen, (50, 50, 50), wall)

    
    pygame.display.flip()  # Atualiza a tela

pygame.quit()
