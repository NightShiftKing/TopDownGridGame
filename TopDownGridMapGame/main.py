import pygame
import numpy as np

pygame.init()
pygame.display.set_caption("Top Down Grid Game")

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

gameOver = False

dirt = pygame.image.load('dirt.jpg')
brick = pygame.image.load('brick.jpg')

map = np.random.randint(0,3, size =(10,10))

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    for i in range(10):
        for j in range(10):
            if map[i][j] == 1:
                screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
            if map[i][j] == 2:
                screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
    pygame.display.flip()

pygame.quit()
