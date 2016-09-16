import pygame


class Player(object):

    def __init__(self, screen, color, x, y, size):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.clock = pygame.time.Clock()

        pygame.draw.rect(self.screen, self.color, [self.x,
                                                   self.y,
                                                   self.size,
                                                   self.size])

    def move(self, direction, size):
        if direction == "left":
            self.x -= size
        if direction == "right":
            self.x += size
        if direction == "up":
            self.y -= size
        if direction == "down":
            self.y += size
            pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.size, self.size])

        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.size, self.size])
        pygame.display.update()
