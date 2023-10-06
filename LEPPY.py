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

player_walk_1 = pygame.image.load("characters/walking1.png").convert_alpha()
player_walk_2 = pygame.image.load("characters/walking2.png").convert_alpha()
player_walk_3 = pygame.image.load("characters/walking3.png").convert_alpha()
player_walk_4 = pygame.image.load("characters/walking4.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
for scale in range(len(player_walk)) :
    player_walk[scale] = pygame.transform.scale(player_walk[scale], (96,96))
    player_rect = player_walk[scale].get_rect(midbottom = (150, 560))

player_slash_1 = pygame.image.load("swoosh/slash0.png").convert_alpha()
player_slash_2 = pygame.image.load("swoosh/slash1.png").convert_alpha()
player_slash_3 = pygame.image.load("swoosh/slash2.png").convert_alpha()
player_slash_4 = pygame.image.load("swoosh/slash3.png").convert_alpha()
player_slash = [player_slash_1, player_slash_2, player_slash_3, player_slash_4]
for slash in range(len(player_slash)) :
    player_slash[slash] = pygame.transform.scale(player_slash[slash], (96,96))
    slash_rect = player_slash[slash].get_rect(midbottom = (182, 560))

bg_width = background_surface1.get_width()
ground_width = ground_surface.get_width()

bg_tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
ground_tiles = math.ceil(SCREEN_WIDTH / ground_width) + 1

bg_scroll = 0
ground_scroll = 0

last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

player_gravity = 0

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 560:  
                player_gravity = -20
            if event.key == pygame.MOUSEBUTTONUP :
                print("mouse")
                #for sl in range(player_slash) :
                    #screen.blit(player_slash[sl], slash_rect)

        

    #----------------------------Background----------------------------#

    for i in range(0,bg_tiles) : 
        screen.blit(background_surface1, (i * bg_width + bg_scroll, 0))  #layer1 scroll
        screen.blit(background_surface2, (i * bg_width + bg_scroll, 0))  #layer2 scroll
        screen.blit(background_surface2, (i * bg_width + bg_scroll, 0))  #layer3 scroll
        
    bg_scroll -= 3  #background scrolling magnitude
    if abs(bg_scroll) > bg_width : bg_scroll = 0  #background loop

    for j in range(0,ground_tiles) : 
        screen.blit(ground_surface, (j * ground_width + ground_scroll, 530))  #ground scroll

    ground_scroll -= 6  #ground scrolling magnitude
    if abs(ground_scroll) > ground_width : ground_scroll = 0  #ground loop

    #-----------------------------Animation-----------------------------#

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:  #calculating ms difference
        frame += 1
        last_update = current_time
        if(frame == 4) : frame = 0  #animation loop

    screen.blit(player_walk[frame], player_rect)  #iterating through list of animation images

    #------------------------------Gameplay------------------------------#


    #--------------------------------------------------------------------#

    #---------Gravity--------#
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 560 : player_rect.bottom = 560

    pygame.display.update()
    
pygame.QUIT()

