import pygame
from player import Player


class Event(object):

    @staticmethod
    def player_event_handler(player1_joystick, player2_joystick, event, player_1, player_2):
        left_counter = right_counter = up_counter = down_counter = 0
        sensitivity = 50
        if event.type == pygame.locals.JOYAXISMOTION:
            player1jx, player1jy = player1_joystick.get_axis(0), player1_joystick.get_axis(1)
            if player1jx < 0:
                left_counter += 1
            if player1jx > 0:
                right_counter += 1
            if player1jy < 0:
                up_counter += 1
            if player1jy > 0:
                down_counter += 1
            print("Left: " + left_counter)
            print("Right: " + right_counter)
            print("Up: " + up_counter)
            print("DOwn: " + down_counter)
            print("x: " + player1jx)
            print("y: " + player1jy)
            if left_counter > sensitivity:
                player_1.move('left')
                left_counter = 0
            elif right_counter > sensitivity:
                player_1.move('right')
                right_counter = 0
            elif up_counter > sensitivity:
                player_1.move('up')
                up_counter = 0
            elif down_counter > sensitivity:
                player_1.move('down')
                down_counter = 0

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
