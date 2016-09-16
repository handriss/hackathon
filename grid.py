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

    def __init__(self, screen, width, height, piece_count, margin):
        self.screen = screen
        self.net = []
        self.margin = margin

        if width > height:
            print(height)
            print(piece_count)
            print(self.margin)
            self.size = height//piece_count
            print(self.size)
            height = self.size - self.margin
            width = width//self.size
            print("Height: " + str(height))
            print("Width: " + str(width))
        else:
            self.size = width//(piece_count + self.margin)
            width = piece_count
            height = height//self.size

        # print(self.size)
        for row in range(3):
            self.net.append([])
            for column in range(3):
                self.net[row].append(Tile(row, column))

    def draw(self):
        for row in self.net:
            for column in row:
                pygame.draw.rect(self.screen, (random.randint(0, 255), 0, 0), [
                    column.x*(self.size + self.margin), column.y*(self.size+self.margin), self.size, self.size
                    ])

    def __str__(self):
        return str(self.x)
