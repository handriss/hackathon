import pygame

# class Player():
#
#     def __init__(self, colort ):
#         self.color


pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Conquer')
pygame.display.update()

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            game_exit = True


pygame.quit()
quit()