from main import *
import random

class Player():

    def __init__(self):
        self.color = (0, 255, 0)

class Tile():

    def __init__(self, x, y, owner=None):
        self.owner = owner
        self.x = x
        self.y = y
        if owner:
            self.color = owner.color
        else:
            self.color = (105, 105, 105)

    def __str__(self):
        return str("x: " + str(self.x) + " y: " + str(self.y))


class Grid():

    def __init__(self, screen, width, height, piece_count, margin):
        self.screen = screen
        self.net = []
        self.margin = margin

        if width > height:
            self.size = height//piece_count
            height = self.size
            piece_count_column = width//self.size
            piece_count_row = piece_count
        else:
            self.size = width//piece_count
            width = self.size
            piece_count_row = height//self.size
            piece_count_column = piece_count

        for row in range(piece_count_column):
            self.net.append([])
            for column in range(piece_count_row):
                self.net[row].append(Tile(row, column))

    def draw(self):
        for row in self.net:
            for column in row:
                pygame.draw.rect(self.screen, column.color, [
                    column.x*(self.size), column.y*(self.size), self.size-self.margin, self.size-self.margin
                    ])

    def __str__(self):
        return str(self.x)
