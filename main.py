import os, sys
import pygame
from grid import *
from pygame.locals import *
from player import Player
from event import Event

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

WHITE = (255,255,255)


class PyManMain:
    """The Main Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=792, height=600):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        self.grid = Grid(self.screen, self.width, self.height, 25, 2)

    def main_loop(self):
        """This is the Main Loop of the Game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            self.grid.draw()
            player_1 = Player(self.screen, (255, 255, 0), self.grid.net[0][0].x * self.grid.size,
                                                          self.grid.net[0][0].y * self.grid.size,
                                                          self.grid.size - self.grid.margin

                              )
            player_2 = Player(self.screen, (255, 255, 0), self.grid.net[-1][-1].x * self.grid.size,
                                                          self.grid.net[-1][-1].y * self.grid.size,
                                                          self.grid.size - self.grid.margin)
            self.grid.count_colors()
            Event.main_event_handler(player_1, player_2, self.grid.size)
            pygame.display.update()


if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.main_loop()
