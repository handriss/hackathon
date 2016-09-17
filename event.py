import pygame
from player import Player
import time


class Event(object):

    @staticmethod
    def player_event_handler(player1_joystick, player2_joystick, event, player_1, player_2):

        if event.type == pygame.locals.JOYAXISMOTION:
            player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
            time.sleep(0.05)
            if player1jx < 0:
                player_1.move('left')
            if player1jx > 0:
                player_1.move('right')
            if player1jy < 0:
                player_1.move('up')
            if player1jy > 0:
                player_1.move('down')
            player2jx, player2jy = player2_joystick.get_axis(0)/10, player2_joystick.get_axis(1)
            if player2jx < 0:
                player_2.move('left')
            if player2jx > 0:
                player_2.move('right')
            if player2jy < 0:
                player_2.move('up')
            if player2jy > 0:
                player_2.move('down')

        # if event.key == pygame.K_LEFT:
        #     player_1.move('left')
        # elif event.key == pygame.K_a:
        #     player_2.move('left')
        # elif event.key == pygame.K_RIGHT:
        #     player_1.move('right')
        # elif event.key == pygame.K_d:
        #     player_2.move('right')
        # elif event.key == pygame.K_UP:
        #     player_1.move('up')
        # elif event.key == pygame.K_w:
        #     player_2.move('up')
        # elif event.key == pygame.K_DOWN:
        #     player_1.move('down')
        # elif event.key == pygame.K_s:
        #     player_2.move('down')

        return player_1, player_2

    @staticmethod
    def tile_event_handler(player, net):
        net[player.x][player.y].update_owner(player)

        return net
