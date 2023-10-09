import pygame
import math
from random import randint, choice

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

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "vulture":
            vulture_walk_1 = pygame.image.load("Vulture_walk/vulture0.png").convert_alpha()
            vulture_walk_2 = pygame.image.load("Vulture_walk/vulture1.png").convert_alpha()
            vulture_walk_3 = pygame.image.load("Vulture_walk/vulture2.png").convert_alpha()
            vulture_walk_4 = pygame.image.load("Vulture_walk/vulture3.png").convert_alpha()
            self.frames = [vulture_walk_1, vulture_walk_2, vulture_walk_3, vulture_walk_4]
            y_pos = 450

        elif type == "snake":
            snake_walk_1 = pygame.image.load("Snake_walk/snake0.png").convert_alpha()
            snake_walk_2 = pygame.image.load("Snake_walk/snake1.png").convert_alpha()
            snake_walk_3 = pygame.image.load("Snake_walk/snake2.png").convert_alpha()
            snake_walk_4 = pygame.image.load("Snake_walk/snake3.png").convert_alpha()
            self.frames = [snake_walk_1, snake_walk_2, snake_walk_3, snake_walk_4]
            y_pos = 550

        elif type == "hyena":
            hyena_walk_1 = pygame.image.load("Hyena_walk/hyena0.png").convert_alpha()
            hyena_walk_2 = pygame.image.load("Hyena_walk/hyena1.png").convert_alpha()
            hyena_walk_3 = pygame.image.load("Hyena_walk/hyena2.png").convert_alpha()
            hyena_walk_4 = pygame.image.load("Hyena_walk/hyena3.png").convert_alpha()
            hyena_walk_5 = pygame.image.load("Hyena_walk/hyena4.png").convert_alpha()
            hyena_walk_6 = pygame.image.load("Hyena_walk/hyena5.png").convert_alpha()
            self.frames = [hyena_walk_1, hyena_walk_2, hyena_walk_3, hyena_walk_4, hyena_walk_5, hyena_walk_6]
            y_pos = 550
        
        elif type == "scorpion":
            scorpion_walk_1 = pygame.image.load("Scorpio_walk/scorpion0.png").convert_alpha()
            scorpion_walk_2 = pygame.image.load("Scorpio_walk/scorpion1.png").convert_alpha()
            scorpion_walk_3 = pygame.image.load("Scorpio_walk/scorpion2.png").convert_alpha()
            scorpion_walk_4 = pygame.image.load("Scorpio_walk/scorpion3.png").convert_alpha()
            self.frames = [scorpion_walk_1, scorpion_walk_2, scorpion_walk_3, scorpion_walk_4]
            y_pos = 550

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(SCREEN_WIDTH, 1500), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if(self.animation_index >= len(self.frames)): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 7
        self.destroy()
    
    def destroy(self):
        if self.rect.x < -100: self.kill()

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

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

score_font = pygame.font.Font("Fonts/BungeeSpice.ttf", 50)
title_font = pygame.font.Font("Fonts/BungeeSpice.ttf", 100)

background_surface = pygame.image.load("Forest/layered_forest0.png").convert_alpha()

"""
player_slash_1 = pygame.image.load("swoosh/slash0.png").convert_alpha()
player_slash_2 = pygame.image.load("swoosh/slash1.png").convert_alpha()
player_slash_3 = pygame.image.load("swoosh/slash2.png").convert_alpha()
player_slash_4 = pygame.image.load("swoosh/slash3.png").convert_alpha()
player_slash = [player_slash_1, player_slash_2, player_slash_3, player_slash_4]
"""

ground_surface = pygame.image.load("tileset/ground2.png").convert()
ground_surface = pygame.transform.scale(ground_surface, (128,128))
ground_rect = ground_surface.get_rect(bottomleft = (0, SCREEN_HEIGHT))
                                         

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

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1800)

while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    current_slash_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["snake", "scorpion", "hyena", "vulture"])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                #snake_rect.left = 1100
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

        obstacle_group.draw(screen)
        obstacle_group.update()

        #------------------------------Gameplay------------------------------#
                
                

        #--------------------------------------------------------------------#

    else:
        if(score == 0):
            game_start()
        else:
            game_over()

    pygame.display.update()
