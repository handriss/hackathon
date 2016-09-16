class Grid():

    def __init__(self, width, height, size):
        self.x = [[[None]*(width//size)]*(height//size)]

    def __str__(self):
        return str(self.x)
