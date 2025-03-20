import pygame
import math

# Configurações iniciais
FPS = 60

# Inicializa o Pygame
pygame.init()

# Configurações de tela
info = pygame.display.Info()  # Obtém informações sobre a resolução do monitor
WIDTH, HEIGHT = info.current_w, info.current_h

# Cria a janela em modo fullscreen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Dead By AI light")
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classe base para personagens
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, color, radius=20):
        super().__init__()
        # Criar uma superfície quadrada para conter o círculo
        self.radius = radius
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        
        # Desenhar o círculo na superfície
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        
        # Definir o retângulo com base na superfície criada
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3  # Velocidade base

    def move(self, keys, left, right, up, down):
        # Definir componentes do movimento
        dx = (keys[right] - keys[left])  # +1 para direita, -1 para esquerda
        dy = (keys[down] - keys[up])  # +1 para baixo, -1 para cima

        # Normalizar o vetor de movimento
        magnitude = math.sqrt(dx**2 + dy**2)  # Calcula a magnitude
        if magnitude > 0:  # Evita divisão por zero
            dx = (dx / magnitude) * self.speed
            dy = (dy / magnitude) * self.speed

        # Atualizar posição
        self.rect.x += dx
        self.rect.y += dy

# Criar o Killer e o Survivor com raio apropriado
killer = Character(100, 100, (255, 0, 0), 20)  # Vermelho para o Killer
survivor = Character(300, 300, (0, 0, 255), 20)  # Azul para o Survivor

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
    killer.move(keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    survivor.move(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

    # Renderização
    screen.fill(WHITE)  # Fundo branco
    all_sprites.draw(screen)  # Desenha os personagens na tela
    
    pygame.display.flip()  # Atualiza a tela

pygame.quit()
