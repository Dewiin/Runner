import pygame
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("LEPPY")
clock = pygame.time.Clock()

background_surface1 = pygame.image.load("Forest/Layers/back.png").convert_alpha()
background_surface2 = pygame.image.load("Forest/Layers/far.png").convert_alpha()
background_surface3 = pygame.image.load("Forest/Layers/middle.png").convert_alpha()

background_surface1 = pygame.transform.scale(background_surface1, (432, 720))
background_surface2 = pygame.transform.scale(background_surface2, (528, 720))

ground_surface = pygame.image.load("tileset/ground2.png").convert()
ground_surface = pygame.transform.scale(ground_surface, (128,128))
ground_rect = ground_surface.get_rect(bottomleft = (0, SCREEN_HEIGHT))

player_surface = pygame.image.load("characters/walking1.png").convert_alpha()
player_surface = pygame.transform.scale(player_surface, (96,96))
player_rect = player_surface.get_rect(midbottom = (100, 560))

bg_width = background_surface1.get_width()
ground_width = ground_surface.get_width()

bg_tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
ground_tiles = math.ceil(SCREEN_WIDTH / ground_width) + 1

bg_scroll = 0
ground_scroll = 0

run = True
while run:
    clock.tick(60)

    for i in range(0,bg_tiles) : 
        screen.blit(background_surface1, (i * bg_width + bg_scroll, 0))
        screen.blit(background_surface2, (i * bg_width + bg_scroll, 0))
        screen.blit(background_surface2, (i * bg_width + bg_scroll, 0))
        
    bg_scroll -= 3
    if abs(bg_scroll) > bg_width : bg_scroll = 0
    for j in range(0,ground_tiles) : screen.blit(ground_surface, (j * ground_width + ground_scroll, 530))
    ground_scroll -= 7
    if abs(ground_scroll) > ground_width : ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(player_surface, player_rect)

    pygame.display.update()
    
pygame.QUIT()

