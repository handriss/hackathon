import pygame
from player import Player


class Event(object):
    left_counter = right_counter = up_counter = down_counter = 0

    @staticmethod
    def player_event_handler(player1_joystick, player2_joystick, event, player_1, player_2):

        sensitivity = 200
        if event.type == pygame.locals.JOYAXISMOTION:
            player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
            if player1jx < 0:
                player_1.move('left')
                Event.left_counter += 1
            if player1jx > 0:
                player_1.move('right')
                Event.right_counter += 1
            # if player1jy < 0:
            #     up_counter += 1
            # if player1jy > 0:
            #     down_counter += 1
            print("Left: " + str(left_counter))
            print("Right: " + str(right_counter))
            print("Up: " + str(up_counter))
            print("DOwn: " + str(down_counter))
            print("x: " + str(player1jx))
            print("y: " + str(player1jy))
            if Event.left_counter > sensitivity:
                player_1.move('left')
                Event.left_counter = 0
            elif Event.right_counter > sensitivity:
                player_1.move('right')
                Event.right_counter = 0
            # elif up_counter > sensitivity:
            #     player_1.move('up')
            #     up_counter = 0
            # elif down_counter > sensitivity:
            #     player_1.move('down')
            #     down_counter = 0

        return player_1, player_2

    @staticmethod
    def tile_event_handler(player, net):
        net[player.x][player.y].update_owner(player)

        return net
