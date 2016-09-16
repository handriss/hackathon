import os
import sys
import pygame
from grid import *
from pygame.locals import *

# if not pygame.font: print('Warning, fonts disabled')
# if not pygame.mixer: print('Warning, sound disabled')

WHITE = (255, 255, 255)


class PyManMain:
    """The Main Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=1000, height=600):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        start_width = 100
        start_height = 50
        self.grid = Grid(
            self.screen, start_width, start_height, self.width-start_width*2, self.height-start_height, 20, 2
            )

    def main_loop(self):
        """This is the Main Loop of the Game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.grid.draw()
            self.grid.count_colors()
            pygame.display.update()


if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.main_loop()
