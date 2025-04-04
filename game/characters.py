import pygame
import math

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, speed):
        """
        Inicializa um personagem genérico.
        - x, y: Posição inicial.
        - radius: Raio do círculo que representa o personagem.
        - color: Cor do personagem.
        - speed: Velocidade base.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.base_speed = speed  # Velocidade original
        self.speed_timer = 0  # Timer para mudanças temporárias de velocidade
        self.direction = pygame.math.Vector2(0, 0)

        # Criação da superfície e do retângulo
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, dx, dy):
        """
        Move o personagem em uma direção normalizada.
        - dx, dy: Direção do movimento.
        """
        self.direction = pygame.math.Vector2(dx, dy)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed
        self.rect.center = (self.x, self.y)

    def change_speed_temp(self, new_speed, seconds, current_game_fps):
        """
        Altera temporariamente a velocidade do personagem.
        - new_speed: Nova velocidade.
        - seconds: Duração do efeito em segundos.
        - current_game_fps: FPS do jogo para calcular a duração em frames.
        """
        duration_frames = seconds * current_game_fps
        self.speed = new_speed
        self.speed_timer = duration_frames

    def update(self):
        """
        Atualiza o estado do personagem, incluindo mudanças temporárias de velocidade.
        """
        if self.speed_timer > 0:
            self.speed_timer -= 1
            if self.speed_timer == 0:
                self.speed = self.base_speed


class Killer(Character):
    def __init__(self, x, y, color, radius=20, speed=3.2):
        super().__init__(x, y, radius, color, speed)
        self.atk_range = 50
        self.atk_angle = 45 # TODO implementar depois hitbox apenas na frente do killer
        self.atk_cooldown = 60
        self.last_atk_time = 0
        self.grab_range = radius + 5

        #Espada
        self.sword_img = pygame.image.load("./assets/killer/espadaJogo.png").convert_alpha()
        self.show_sword = False
        self.sword_timer = 0
        self.sword_duration = 15
    
    def attack(self, survivor):
        self.show_sword = True
        self.sword_timer = self.sword_duration
        hitbox = self.get_attack_hitbox()
        survivor_rect = survivor.rect
        if hitbox.colliderect(survivor_rect):
            return True  # Acertou
        return False  # Errou

    
    def get_attack_hitbox(self):
    
        direction = self.direction if self.direction.length() > 0 else pygame.Vector2(1, 0)  # padrão direita
        direction = direction.normalize()
        hitbox_length = 40  # distância à frente
        hitbox_width = 30  # largura da hitbox
        # Calcula o centro da hitbox
        hitbox_center = pygame.Vector2(self.x, self.y) + direction * (self.radius + hitbox_length / 2)
        hitbox_rect = pygame.Rect(0, 0, hitbox_length, hitbox_width)
        hitbox_rect.center = hitbox_center
        return hitbox_rect



    def grab_survivor(self, survivor):
        distance = math.hypot(survivor.x - self.x, survivor.y - self.y)
        if distance <= self.grab_range:
            survivor.grabbed = True
            survivor.x = self.x + self.radius + survivor.radius
            survivor.y = self.y
            survivor.rect.center = (survivor.x, survivor.y)
            return True
        return False
    
    def update(self):
        super().update()
        if self.sword_timer > 0:
            self.sword_timer -= 1
        else:
            self.show_sword = False



    def distance(self, other):
        return math.hypot(other.x - self.x, other.y - self.y)

class Survivor(Character):
    def __init__(self, x, y, color, radius, speed):
        super().__init__(x, y, radius, color, speed)
        self.color = color
        self.speed = speed
        self.base_speed = speed
        self.health = 100
        self.health_state = 1 
        # 1 = healthy
        # 2 = injured
        # 3 = downed
        self.hooked = False
        self.hook_health_state = 1
        # 1 = never hooked
        # 2 = hooked 1 time
        # 3 = hooked 2 times
        # 4 = dead
        self.grabbed = False
    
    def heal(self, other_survivor):
        if self.distance(other_survivor) <= 50 and self.health_state < 3 and other_survivor.health < 3:
            return True
        return False

    def repair_gen(self, generator):
        if self.distance(generator) <= 50:
            return True
        return False