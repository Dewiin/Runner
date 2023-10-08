import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("characters/walking1.png").convert_alpha()
        player_walk_2 = pygame.image.load("characters/walking2.png").convert_alpha()
        player_walk_3 = pygame.image.load("characters/walking3.png").convert_alpha()
        player_walk_4 = pygame.image.load("characters/walking4.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
        self.walk_frame = 0

        self.image = self.player_walk[self.walk_frame]
        self.rect = self.image.get_rect(midbottom = (200, 500))
        self.gravity = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 500:
            self.gravity = -22
        if keys[pygame.K_a]:
            self.rect.x -= 6
            if self.rect.x < 0: self.rect.x = 0
        if keys[pygame.K_d]:
            self.rect.x += 6
            if self.rect.right >= SCREEN_WIDTH-50: self.rect.right = SCREEN_WIDTH-50
        
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 500: self.rect.bottom = 500

    def animation_state(self):
        self.walk_frame += 0.1
        if self.walk_frame >= len(self.player_walk): self.walk_frame = 0
        self.image = self.player_walk[int(self.walk_frame)]
        self.image = pygame.transform.scale(self.image, (96,96))

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

"""
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super()__init__()
"""


def display_score():
    current_time = int(pygame.time.get_ticks()/500) - int(start_time/500)
    score_surface = score_font.render(f'{current_time}', False, "Orange")
    score_rect = score_surface.get_rect(center = (SCREEN_WIDTH/2, 100))
    screen.blit(score_surface, score_rect)
    return current_time

def game_over():
    screen.fill("Black")
    game_over_surface = pygame.image.load("GameOver.png").convert_alpha()
    game_over_rect = game_over_surface.get_rect(center = (SCREEN_WIDTH/2, 150))
    game_score_surface = score_font.render(f"Score: {score}", False, "White")
    game_score_rect = game_score_surface.get_rect(center = (SCREEN_WIDTH/2, 300))
    restart_surface = score_font.render("Press enter to restart", False, "White")
    restart_rect = restart_surface.get_rect(center = (SCREEN_WIDTH/2, 450))
    
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(game_score_surface, game_score_rect)
    screen.blit(restart_surface, restart_rect)

def game_start():
    title_surface = title_font.render("LEPPY", False, "Orange")
    title_rect = title_surface.get_rect(center = (SCREEN_WIDTH/2, 100))
    screen.fill("Black")
    screen.blit(title_surface, title_rect)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("LEPPY")
clock = pygame.time.Clock()
start_time = 0
score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

score_font = pygame.font.Font("Fonts/BungeeSpice.ttf", 50)
title_font = pygame.font.Font("Fonts/BungeeSpice.ttf", 100)

background_surface = pygame.image.load("Forest/layered_forest0.png").convert_alpha()

ground_surface = pygame.image.load("tileset/ground2.png").convert()
ground_surface = pygame.transform.scale(ground_surface, (128,128))
ground_rect = ground_surface.get_rect(bottomleft = (0, SCREEN_HEIGHT))

"""
player_slash_1 = pygame.image.load("swoosh/slash0.png").convert_alpha()
player_slash_2 = pygame.image.load("swoosh/slash1.png").convert_alpha()
player_slash_3 = pygame.image.load("swoosh/slash2.png").convert_alpha()
player_slash_4 = pygame.image.load("swoosh/slash3.png").convert_alpha()
player_slash = [player_slash_1, player_slash_2, player_slash_3, player_slash_4]
"""

snake_walk_1 = pygame.image.load("Snake_walk/snake0.png").convert_alpha()
snake_walk_2 = pygame.image.load("Snake_walk/snake1.png").convert_alpha()
snake_walk_3 = pygame.image.load("Snake_walk/snake2.png").convert_alpha()
snake_walk_4 = pygame.image.load("Snake_walk/snake3.png").convert_alpha()
snake_walk = [snake_walk_1, snake_walk_2, snake_walk_3, snake_walk_4]
for sn in range (len(snake_walk)): 
    snake_walk[sn] = pygame.transform.scale(snake_walk[sn], (144,144))
    snake_rect = snake_walk[sn].get_rect(bottomleft = (SCREEN_WIDTH, 540))
                                         

bg_width = 432
ground_width = ground_surface.get_width()

bg_tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
ground_tiles = math.ceil(SCREEN_WIDTH / ground_width) + 1

bg_scroll = 0
ground_scroll = 0

last_slash_update = pygame.time.get_ticks()
slash_cooldown = 1000
slash_frame = 0

run = True
game_active = False

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
                #player_rect = 0
                start_time = current_time
                game_active = True
                

    #----------------------------Background----------------------------#
    if game_active:
        score = display_score()

        for i in range(0,bg_tiles) : 
            screen.blit(background_surface, (i * bg_width + bg_scroll, 0))  #tree background
            
        bg_scroll -= 3  #background scrolling magnitude
        if abs(bg_scroll) > bg_width : bg_scroll = 0  #background loop

        for j in range(0,ground_tiles) : 
            screen.blit(ground_surface, (j * ground_width + ground_scroll, 530))  #ground scroll

        ground_scroll -= 5  #ground scrolling magnitude
        if abs(ground_scroll) > ground_width : ground_scroll = 0  #ground loop

        display_score()

        #-----------------------------Animation-----------------------------#

        player.draw(screen)
        player.update()

        #------------------------------Gameplay------------------------------#
                
                

        #--------------------------------------------------------------------#

    else:
        if(score == 0):
            game_start()
        else:
            game_over()

    pygame.display.update()
