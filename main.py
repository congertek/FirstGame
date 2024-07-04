import pygame
from random import randint
from os.path import join

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

# Plain Surface
surf = pygame.Surface((100, 200))
surf.fill('green')
x = 100

# Imports
player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surface.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 1)
player_speed = 300

star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(50)]

meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surface.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surface = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surface.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
           print(1)
        #if event.type == pygame.MOUSEMOTION:
        #   player_rect.center = event.pos

   # Input
   # print(pygame.mouse.get_rel())
   # keys = pygame.key.get_pressed()
   # if keys[pygame.K_1]:
   #     print(1)


    # draw the game
    display_surface.fill('grey20')
    for pos in star_positions:
        display_surface.blit(star_surface, pos)

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)
    display_surface.blit(player_surface, player_rect)

    pygame.display.update()

pygame.quit()
