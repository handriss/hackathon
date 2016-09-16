from main import *
import random


class Tile():

    def __init__(self, x, y, owner=None):
        self.owner = owner
        self.x = x
        self.y = y

    def __str__(self):
        return str("x: " + str(self.x) + " y: " + str(self.y))


class Grid():

    def __init__(self, screen, width=10, height=20, size=5):
        self.screen = screen
        self.net = []
        self.size = size
        for row in range(width//size):
            self.net.append([])
            for column in range(height//size):
                self.net[row].append(Tile(row, column))

    def draw(self):
        for row in self.net:
            for column in row:
                pygame.draw.rect(self.screen, (random.randint(0,255),0,0), [column.x*self.size, column.y*self.size, self.size, self.size])
                print(column.x, column.y)

    def __str__(self):
        return str(self.x)


