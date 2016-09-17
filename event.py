import pygame
from player import Player


class Event(object):
    left = True
    right = True

    @staticmethod
    def player_event_handler(mozoghatsz, player1_joystick, player2_joystick, event, player_1, player_2):
        if player1_joystick.get_button(0):
            player_1.move('right')

        if event.type == pygame.locals.JOYAXISMOTION:
            player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
            if player1jx < 0:
                player_1.move('left')
                mozoghatsz = False
            elif player1jy > 0:
                player_1.move('right')
                mozoghatsz = False

        return mozoghatsz, player_1, player_2

    @staticmethod
    def tile_event_handler(player, net):
        net[player.x][player.y].update_owner(player)

        return net
