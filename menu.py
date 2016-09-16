import pygame
import sys
from pygame.locals import *


class Option:
    hovered = False

    def __init__(self, text, pos, select):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
        self.select = select

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def select(self):
        if self.select:
            return True

pygame.init()
screen = pygame.display.set_mode((480, 320))
menu_font = pygame.font.Font(None, 40)
options = [Option("SINGLEPLAYER", (140, 105), 0), Option("MULTIPLAYER", (135, 155), 1),
           Option("EXIT", (145, 205), 2)]

select = 0
while True:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for option in options:
        if option.select == select:
            option.hovered = True
        else:
            option.hovered = False
        if event.type == pygame.KEYDOWN:
            if (event.key == K_0):
                select = 0
            elif (event.key == K_1):
                select = 1
            elif (event.key == K_2):
                select = 2
                quit()
        option.draw()
    pygame.display.update()

# option = 1
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             option += 1
#         if event.type == pygame.KEYUP:
#             option -= 1
#