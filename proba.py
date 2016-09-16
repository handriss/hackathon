import pygame
import sys
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20

MARGIN = 2

grid = []
for row in range(50):
    grid.append([])
    for column in range(50):
        grid[row].append(0)

grid[1][5] = 1

pygame.init()

WINDOW_SIZE = [800, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Játékunk")

done = False

clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
        elif event.type == pygame.KEYDOWN:
            if (event.key == K_RIGHT):
                print("k-right")
            elif (event.key == K_LEFT):
                print("k-left")
            elif (event.key == K_UP):
                print("k-up")
            elif (event.key == K_DOWN):
                print("k-down")

    screen.fill(BLACK)

    for row in range(50):
        for column in range(50):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
