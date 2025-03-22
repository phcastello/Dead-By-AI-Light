import pygame
import math

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, speed):
        super().__init__()  # Inicializa o construtor da classe base pygame.sprite.Sprite
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.health = 1  # Default health for all characters
        self.direction = pygame.math.Vector2(0, 0)

        # Cria a superfície e o retângulo para o sprite
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, dx, dy):
        # Normalize movement
        self.direction = pygame.math.Vector2(dx, dy)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed
        self.rect.center = (self.x, self.y)  # Atualiza a posição do retângulo


class Killer(Character):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color, speed=3.5)
        self.atk_range = 50
        self.atk_angle = 45  # In degrees
        self.atk_cooldown = 60 # In frames (1s at 60 FPS)
        self.last_attack_time = 0

    def attack(self, target, current_time):
        if current_time - self.last_attack_time >= self.atk_cooldown:
            # Calculate distance and angle to the target
            distance = math.hypot(target.x - self.x, target.y - self.y)
            angle = math.degrees(math.atan2(target.y - self.y, target.x - self.x))
            if distance <= self.atk_range and abs(angle) <= self.atk_angle / 2:
                self.last_attack_time = current_time
                return True  # Attack successful
        return False


class Survivor(Character):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color, speed=3.0)
        self.health = 3

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.health = 0  # Survivor is "dead"