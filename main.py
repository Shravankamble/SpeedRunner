import pygame
# import collision
import values
from sys import exit

pygame.init()
# size of the window or display
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
# score
# game_loop
game_loop = True
font_name = pygame.font.Font(None, 35)
score_render = font_name.render('SCORE', False, 'black')
score_rect = score_render.get_rect(center = (545, 20))
# game_over
# game_over = font_name.render('GAME OVER', False, 'black')
# game_over_rect = game_over.get_rect(center = (600, 300))
# the title of the game
pygame.display.set_caption('SpeedRunner')
# we are never gonna move the main image it gonna be where it was from the starting
pygame_logo = pygame.image.load('run.png')
pygame.display.set_icon(pygame_logo)
# background/sky
sky_image = pygame.image.load('sky_image.png')
# airplane
airplane = pygame.image.load('airplane.png').convert_alpha()
# cloud
cloud = pygame.image.load('cloudy.png').convert_alpha()
# extra cloud
extra_clouds = pygame.image.load('clouds.png').convert_alpha()
# sun
sun = pygame.image.load('contrast.png').convert_alpha()
# ground
ground = pygame.image.load('ground.png')
# extra ground
extra_ground = pygame.image.load('extra_ground.png')
# tree
tree = pygame.image.load('tree.png').convert_alpha()
#house
house = pygame.image.load('house.png').convert_alpha()
#family of that house
family_of_that_house = pygame.image.load('garden.png').convert_alpha()
# player
player = pygame.image.load('ninja.png').convert_alpha()
player_rect = player.get_rect(midbottom = (35, 502))
# car
car = pygame.image.load('cactus.png').convert_alpha()
car_rect = car.get_rect(bottomright = (1000, 502))
# game_over
# game_over = pygame.image.load('game_over.png').convert_alpha()
# game_over_rect = game_over.get_rect(center = (1500, 300))
# 545
# black hole
black_hole = pygame.image.load('black-hole.png').convert_alpha()
black_hole_rect = black_hole.get_rect(midbottom = (700, 460))
# player_x and player_y
player_x = 35
player_y = 445
# family_of_that_house_x
family_of_that_house_x = 555
# house_x
house_x = 565
# tree_x
tree_x = 5
# ground_x
ground_y = 500
## car_x = 1300
# sun_x
sun_x = -10
# extra_clouds_x
extra_clouds_x = 900
# cloud_x
cloud_x = 1100
# airplane_x
airplane_x = 0
# gravity
flat_surface = 0
Tick = pygame.time.Clock()

# trying out co-ordinates to learn more about them 
# aquiring space is (100, 200) for that you use pygame.Surface
# this is just to have an idea that how work with co-ordinates
# no need of this just practicing.
# testing = pygame.Surface((100, 200))
# the fill is just means adding color to it
# testing.fill('white')

# this is the while loop to run display until the user quits means exiting the game.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                flat_surface = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 502:
                flat_surface = -20
            
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         player_rect.right += 20
        #         if player_rect.right > 1300:
        #             player_rect.left = 0

    # .blit() basically means adding additional surface on each other.
    # screen.blit(testing, (10, 500))
    # bg_image/sky
    if game_loop:
        screen.blit(sky_image, (0, 0))
        airplane_x += 1
        if airplane_x > 2000:
            airplane_x = values.airplane_respawn_pos
        # airplane
        screen.blit(airplane, (airplane_x, 120))
        # cloud
        screen.blit(cloud, (cloud_x, 120))
        cloud_x -= 0.1
        if cloud_x < -185:
            cloud_x = values.cloud_x_respawn_pos
        # extra_cloud
        screen.blit(extra_clouds, (extra_clouds_x, 129))
        # sun
        screen.blit(sun, (sun_x, 0))
        # score_render
        screen.blit(score_render, score_rect)
        # ground
        screen.blit(ground, (0, ground_y))
        # extra_ground
        screen.blit(extra_ground, (800, ground_y))
        # tree
        screen.blit(tree, (tree_x, 380))
        # house
        screen.blit(house, (house_x, 380))
        # family_of_that_house
        screen.blit(family_of_that_house, (family_of_that_house_x, 471))
        # screen.blit(black_hole, black_hole_rect)
        # car object
        screen.blit(car, car_rect)
        # player 
        flat_surface += 1
        player_rect.y += flat_surface
        if player_rect.bottom > 502:
            player_rect.bottom = 502
        screen.blit(player, player_rect)
        # keys = pygame.key.get_pressed()
        # 67
        # print(player_rect.right)
        # house movement
        house_x += 4
        if house_x > 1300:
            house_x = values.house_x_respawn_pos

        # family_of_that_house movement
        family_of_that_house_x += 4
        if family_of_that_house_x > 1300:
            family_of_that_house_x = values.family_of_that_house_x_respawn_pos

        # tree movement
        tree_x += 4
        if tree_x > 1300:
            tree_x = values.tree_x_respawn_pos

        # black_hole
        # black_hole_rect.x += 1
        # if black_hole_rect.right > 3000:
        #     black_hole_rect.left = 10000

        # car mechanism
        car_rect.x -= 6
        if car_rect.right < -200:
            car_rect.left = 1300

        # cloud movement
        extra_clouds_x -= 0.1
        if extra_clouds_x < -200:
            extra_clouds_x = values.extra_cloud_respawn_pos

        if player_rect.colliderect(car_rect):
            game_loop = False
            screen.fill('black')
            # screen.blit(game_over, game_over_rect)
    # pygame.display.update() is used to keep updating the screen or display
    pygame.display.update()
    # ths .tick() function is used for the games fps(frames per second)
    Tick.tick(80)