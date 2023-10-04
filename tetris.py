import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000,700))

while True:
    for tails in pygame.event.get():
        if tails.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()




