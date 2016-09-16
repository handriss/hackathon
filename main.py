import os
import sys
import pygame
from view import *
from pygame.locals import *

WHITE = (255, 255, 255)


class PyManMain:

    def __init__(self, width=1000, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))

        clock = pygame.time.Clock()
        counter, text = 10, '10'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont('Consolas', 30)

        menu_width = 100
        menu_height = 50
        self.menu = Menu(menu_width, menu_height)

        self.grid = Grid(
            self.screen, menu_width, menu_height, self.width-menu_width*2, self.height-menu_height, 20, 2
            )
        self.menu.countdown(10)

    def main_loop(self):
        """This is the Main Loop of the Game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.grid.draw()
            self.grid.count_colors()
            pygame.display.update()


if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.main_loop()

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        continue
    break
