class Tile():

    def __init__(self, x, y, owner=None):
        self.owner = owner
        self.x = x
        self.y = y

    def __str__(self):
        return str("x: " + str(self.x) + " y: " + str(self.y))


class Grid():

    def __init__(self, width=10, height=20, size=5):
        self.x = []
        for row in range(width//size):
            print(row)
            self.x.append([])
            for column in range(height//size):
                print(column)
                self.x[row].append(Tile(row, column))
                print(Tile(row, column))

    def __str__(self):
        return str(self.x)

Grid()
