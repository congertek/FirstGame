import pygame
from random import randint
from os.path import join


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def update(self):
        print('ship is being updated')

# General Setup


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

#Create an instance of the Player Class
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

# Imports
# player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
# player_rect = player_surface.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# player_direction = pygame.math.Vector2(1, 1)
# player_speed = 300

star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(50)]

meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surface.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surface = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surface.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))
laser_direction = pygame.math.Vector2(1, 1)

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    # keys = pygame.key.get_pressed()
    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    # player_direction = player_direction.normalize() if player_direction else player_direction
    # player_rect.center += player_direction * player_speed * dt

    # recent_keys = pygame.key.get_just_pressed()
    # if recent_keys[pygame.K_SPACE]:
    #     print('You fired your gun')

    all_sprites.update()

    # draw_the_game
    display_surface.fill('grey20')
    for pos in star_positions:
        display_surface.blit(star_surface, pos)

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)
    # display_surface.blit(player_surface, player_rect)
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
