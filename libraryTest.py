import pygame
import torch
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import gym

# Teste do Pygame - Criar uma janela simples
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test Pygame")

# Teste do PyTorch - Criar um tensor e multiplicar por 2
tensor = torch.tensor([1.0, 2.0, 3.0])
print("PyTorch tensor:", tensor * 2)

# Teste do NumPy - Criar um array e somar 10
array = np.array([4, 5, 6])
print("NumPy array:", array + 10)

# Teste do Matplotlib - Gerar um gráfico simples
plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Matplotlib Test")
plt.show()

# Teste do NetworkX - Criar e desenhar um grafo simples
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])
nx.draw(G, with_labels=True)
plt.title("NetworkX Test")
plt.show()

# Teste do Gym - Criar um ambiente de jogo (CartPole)
env = gym.make("CartPole-v1")
obs = env.reset()
print("Gym environment observation:", obs)

# Loop de eventos do Pygame (fecha ao clicar no X)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
