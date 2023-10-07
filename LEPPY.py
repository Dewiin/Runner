import pygame
import math

def display_score():
    current_time = pygame.time.get_ticks()
    score_surface = score_font.render(f'{current_time}', False, "Orange")
    score_rect = score_surface.get_rect(center = (SCREEN_WIDTH/2, 100))
    screen.blit(score_surface, score_rect)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("LEPPY")
clock = pygame.time.Clock()

score_font = pygame.font.Font("Fonts/BungeeSpice.ttf", 50)

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

snake_walk_1 = pygame.image.load("Snake_walk/snake0.png").convert_alpha()
snake_walk_2 = pygame.image.load("Snake_walk/snake1.png").convert_alpha()
snake_walk_3 = pygame.image.load("Snake_walk/snake2.png").convert_alpha()
snake_walk_4 = pygame.image.load("Snake_walk/snake3.png").convert_alpha()
snake_walk = [snake_walk_1, snake_walk_2, snake_walk_3, snake_walk_4]
for sn in range (len(snake_walk)): 
    snake_walk[sn] = pygame.transform.scale(snake_walk[sn], (144,144))
    snake_rect = snake_walk[sn].get_rect(bottomleft = (SCREEN_WIDTH, 540))
                                         

bg_width = background_surface1.get_width()
ground_width = ground_surface.get_width()

bg_tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
ground_tiles = math.ceil(SCREEN_WIDTH / ground_width) + 1

bg_scroll = 0
ground_scroll = 0

last_update = pygame.time.get_ticks()
last_slash_update = pygame.time.get_ticks()
animation_cooldown = 200
slash_cooldown = 1000
walk_frame = 0
slash_frame = 0

player_gravity = 0

run = True
game_active = True

while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    current_slash_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                snake_rect.left = 1100
                player_rect.bottom = 560
                player_rect.x = 150 
                game_active = True

    #----------------------------Background----------------------------#
    if game_active:
        for i in range(0,bg_tiles) : 
            screen.blit(background_surface1, (i * bg_width + bg_scroll, 0))  #layer1 scroll
            screen.blit(background_surface2, (i * bg_width + bg_scroll, 0))  #layer2 scroll
            screen.blit(background_surface2, (i * bg_width + bg_scroll, 0))  #layer3 scroll
            
        bg_scroll -= 3  #background scrolling magnitude
        if abs(bg_scroll) > bg_width : bg_scroll = 0  #background loop

        for j in range(0,ground_tiles) : 
            screen.blit(ground_surface, (j * ground_width + ground_scroll, 530))  #ground scroll

        ground_scroll -= 5  #ground scrolling magnitude
        if abs(ground_scroll) > ground_width : ground_scroll = 0  #ground loop

        display_score()

        #-----------------------------Animation-----------------------------#

        if current_time - last_update >= animation_cooldown:  #calculating ms difference
            walk_frame += 1
            last_update = current_time
            if(walk_frame == 4) : walk_frame = 0  #animation loop

        screen.blit(player_walk[walk_frame], player_rect)  #iterating through list of animation images
        screen.blit(snake_walk[walk_frame], snake_rect)
        snake_rect.x -= 7
        if snake_rect.x < -500 : snake_rect.x = SCREEN_WIDTH

        #------------------------------Gameplay------------------------------#
            
        keys = pygame.key.get_pressed()
        if(current_slash_time - last_slash_update >= slash_cooldown):
            if keys[pygame.K_j]:
                screen.blit(player_slash[slash_frame], slash_rect)
                slash_frame += 1
                if(slash_frame == 4): 
                    slash_frame = 0
                    last_slash_update = current_slash_time
        if keys[pygame.K_SPACE] and player_rect.bottom >= 560:
            player_gravity = -22
        if keys[pygame.K_a]:
            player_rect.x -= 6
            if player_rect.x < 0: player_rect.x = 0
        if keys[pygame.K_d]:
            player_rect.x += 6
            if player_rect.right > SCREEN_WIDTH: player_rect.right = SCREEN_WIDTH

        for slash in range(len(player_slash)) :
            player_slash[slash] = pygame.transform.scale(player_slash[slash], (96,96))
            slash_rect = player_slash[slash].get_rect(topleft = (player_rect.x + 30, player_rect.y))
                
                        

        #--------------------------------------------------------------------#

        #---------Gravity--------#
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 560 : player_rect.bottom = 560

        #collision
        if(player_rect.colliderect(snake_rect)):
            game_active = False

    else:
        screen.fill("Yellow")


    pygame.display.update()

pygame.QUIT()

