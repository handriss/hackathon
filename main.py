import os
import sys
import pygame
from view import *
from pygame.locals import *
from player import Player
from event import Event


class Main:

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

        self.grid = Grid(self.screen, menu_width, menu_height, self.width-menu_width*2, self.height-menu_height, 5, 2)
        upper_left = (0, 0)
        bottom_right = (self.grid.net[-1][-1].x, self.grid.net[-1][-1].y)
        maximum = bottom_right

        self.player_1 = Player((255, 255, 0), upper_left, maximum)
        self.player_2 = Player((80, 10, 220), bottom_right, maximum)

    def main_loop(self):
        game = True
        while game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                self.player_1, self.player_2 = Event.player_event_handler(event, self.player_1, self.player_2)
                self.grid.net = Event.tile_event_handler(self.player_1, self.grid.net)
                self.grid.net = Event.tile_event_handler(self.player_2, self.grid.net)
                self.grid.draw()

            self.grid.count_colors()

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.main_loop()
