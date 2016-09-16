from main import *
import random


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
                self.net[row].append(Tile(row, column, None))

    def draw(self):
        for row in self.net:
            for column in row:
                pygame.draw.rect(self.screen, column.color, [
                    column.x*(self.size), column.y*(self.size), self.size-self.margin, self.size-self.margin
                    ])

    def count_colors(self):
        owners = {}
        for row in self.net:
            for column in row:
                try:
                    owners[column.owner.name] = owners.get(column.owner.name, 0) + 1
                except AttributeError:
                    owners[None] = owners.get(None, 0) + 1
        return owners

    def __str__(self):
        return str(self.x)
