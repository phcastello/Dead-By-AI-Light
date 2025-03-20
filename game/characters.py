import pygame
import math

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, color, radius=20, speed=3):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.base_speed = speed

    def move(self, keys, up, left, down, right):
        # TODO BUG Killer não tem velocidade de 3.5 para cima e para esquerda, apenas para baixo e direita
        dy = (keys[down] - keys[up])
        dx = (keys[right] - keys[left])

        print(f"\n\n\nImprimindo valores de {self}")
        print(f"Antes da normalização:\ndx: {dx}\ndy:{dy}")
        
        # Normaliza a direção (se houver movimento)
        magnitude = math.sqrt(dx**2 + dy**2)
        print(f"magnitude: {magnitude}")
        if magnitude > 0:
            dx /= magnitude
            dy /= magnitude
        
        print("=================================")
        print(f"Depois da normalização:\ndx: {dx}\n dy:{dy}")
        print("=================================")
        print(f"Velocidade x: {dx * self.speed}")
        print(f"Velocidade y: {dy * self.speed}")

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def change_speed_temporarily(self, new_speed, frames):
        self.speed = new_speed
        self.frames = frames



class Killer(Character):
    def __init__(self, x, y, color, radius=20, speed=3.5):
        super().__init__(x, y, color, radius, speed)
        self.atk_range = 50
        self.atk_angle = 45 # TODO implementar depois hitbox apenas na frente do killer
        self.atk_cooldown = 60
    
    def attack(self, survivor):
        if self.atk_cooldown <= 0 and pygame.key.get_pressed()[pygame.K_e]:
            self.atk_cooldown = 60
            self.color = (128, 128, 0) # Cor de ataque, amarelo
            self.change_speed_temporarily(1, 30) # 0,5 s
            if self.distance(survivor) <= self.atk_range: # hit
                self.change_speed_temporarily(1, 90) # 1,5 s
                survivor.health = max(0, survivor.health - 1)
                    
            
class Survivor(Character):
    def __init__(self, x, y, color, radius=20, speed=3):
        super().__init__(x, y, color, radius, speed)
        self.health = 3
    
    def heal(self, other_survivor):
        if self.distance(other_survivor) <= 50 and self.health < 3 and other_survivor.health > 0:
            if pygame.key.get_pressed()[pygame.K_e]:
                self.health += 1
                other_survivor.health -= 1

    def repair(self, generator):
        if self.distance(generator) <= 50 and pygame.key.get_pressed()[pygame.K_e]:
            while generator.progress < 600:
                generator.progress += 1