import os
import sys
import pygame
from view import *
from pygame.locals import *
from player import Player
from event import Event
import time


class Main:

    def __init__(self, width=1000, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))

        self.clock = pygame.time.Clock()
        self.counter, self.text = 10, '10'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont('comicsansms', 20)

        menu_width = 100
        menu_height = 50
        self.menu = Menu(menu_width, menu_height)

        self.grid = Grid(self.screen, menu_width, menu_height, self.width-menu_width*2, self.height-menu_height, 15, 2)
        upper_left = (0, 0)
        bottom_right = (self.grid.net[-1][-1].x, self.grid.net[-1][-1].y)
        maximum = bottom_right

        self.player_1 = Player((255, 255, 0), upper_left, maximum)
        self.player_2 = Player((80, 10, 220), bottom_right, maximum)

        try:
            pygame.joystick.init()
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            joysticks[0].init()
            joysticks[1].init()
            self.player1_joystick = joysticks[0]
            self.player2_joystick = joysticks[1]
        except IndexError:
            self.player1_joystick = None
            self.player2_joystick = None

    def highscore(self):
        score = self.grid.count_colors()
        self.screen.blit(self.font.render(str(self.player_1.name), True, (255, 255, 255)), (450, 50))
        self.screen.blit(self.font.render(str(score[self.player_1.color]), True, (255, 255, 255)), (495, 80))
        self.screen.blit(self.font.render(str(self.player_2.name), True, (255, 255, 255)), (450, 110))
        self.screen.blit(self.font.render(str(score[self.player_2.color]), True, (255, 255, 255)), (495, 140))

    def main_loop(self):
        self.mozoghatsz = True
        game = True
        while True:
            if game:
                if int(round(time.time() * 1000)) % 1000 == 0:
                    self.mozoghatsz = True
                for event in pygame.event.get():
                    print(event)
                    if event.type == pygame.QUIT:
                        game = False
                    self.mozoghatsz, self.player_1, self.player_2 = Event.player_event_handler(self.mozoghatsz, self.player1_joystick, self.player2_joystick, event, self.player_1, self.player_2)
                    self.grid.net = Event.tile_event_handler(self.player_1, self.grid.net)
                    self.grid.net = Event.tile_event_handler(self.player_2, self.grid.net)
                    self.grid.draw()
                    if event.type == pygame.USEREVENT:
                        self.counter -= 1
                        self.text = str(self.counter).rjust(3) if self.counter > 0 else 'Game Over!'
                        if self.text == 'Game Over!':
                            game = False

                    if event.type == pygame.QUIT:
                        break
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), [self.width/2, 10, 50, 30])
                    self.screen.blit(self.font.render(self.text, True, (255, 255, 255)), (self.width/2, 10))
                    self.screen.blit(self.font.render(self.player_1.name, True, (255, 255, 255)), (20, 20))
                    self.screen.blit(self.font.render(self.player_2.name, True, (255, 255, 255)), (self.width - 100, 20))

                    score = self.grid.count_colors()
                    pygame.draw.rect(self.screen, (0, 0, 0), [20, 50, 50, 50])
                    pygame.draw.rect(self.screen, (0, 0, 0), [self.width-100, 50, 50, 50])
                    self.screen.blit(self.font.render(str(score[self.player_1.color]), True, (255, 255, 255)), (20, 50))
                    self.screen.blit(self.font.render(str(score[self.player_2.color]), True, (255, 255, 255)), (self.width - 100, 50))

                    pygame.display.flip()
                    self.clock.tick(60)
                    continue
                break

                pygame.display.update()
            else:
                self.screen.fill((0, 0, 0))
                self.highscore()
                pygame.display.update()
                time.sleep(3)
                quit()


if __name__ == "__main__":
    main = Main()
    main.main_loop()
