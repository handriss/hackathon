import pygame
from grid import *


class Player():
    '''Everything related to the players'''
    def __init__(self, screen, color, x, y, size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.size, self.size])

    def set_owner(self, tile):
        pass












