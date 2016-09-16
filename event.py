import pygame
from player import Player


class Event(object):
    """Handles keys and movements of sprints/players."""

    @staticmethod
    def main_event_handler(player_1, player_2, size):
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_1.move('left', size)
                    elif event.key == pygame.K_a:
                        player_2.move('left', size)
                    elif event.key == pygame.K_RIGHT:
                        player_1.move('right', size)
                    elif event.key == pygame.K_d:
                        player_2.move('right', size)
                    elif event.key == pygame.K_UP:
                        player_1.move('up', size)
                    elif event.key == pygame.K_w:
                        player_2.move('up', size)
                    elif event.key == pygame.K_DOWN:
                        player_1.move('down', size)
                    elif event.key == pygame.K_s:
                        player_2.move('down', size)
                    else:
                        pass
        pygame.quit()
        quit()
