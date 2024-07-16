import pygame
import random

pygame.init()

# Important variable
X_SIZE = 640
Y_SIZE = 640
FPS = 60
player_position = [300, 580]
player_width = 100
player_height = 10
ball_position = [X_SIZE // 2, Y_SIZE // 2]
speed = [random.uniform(2, 4), random.uniform(2, 4)]

# set the title, icon and bg
logo_image = pygame.image.load("ping-pong.png")
background_image = pygame.image.load("Background.png")
logo = pygame.display.set_icon(logo_image)
title = pygame.display.set_caption("Pong_Game")
ball = pygame.image.load("ball.png")

display = pygame.display.set_mode((X_SIZE, Y_SIZE))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    display.blit(background_image, (0,0))

    # player movement and collision detection
    player = pygame.draw.rect(display, "blue", pygame.Rect(player_position[0], player_position[1], player_width, player_height))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position[0] -= 5
        if player_position[0] < 0:
            player_position[0] = 0

    if keys[pygame.K_RIGHT]:
        player_position[0] += 5
        if player_position[0] > 540:
            player_position[0] = 540


    # make the ball bounch
    display.blit(ball, (ball_position))

    ball_position[0] += speed[0]
    ball_position[1] += speed[1]
    
    if ball_position[0] <= 0 or ball_position[0] >= 620:
        speed[0] = -speed[0]
    if ball_position[1] <= 0:
        speed[1] = -speed[1]

    # bounch from platform
    if player_position[0] <= ball_position[0] <= player_position[0] + player_width and player_position[1] <= ball_position[1] <= player_position[1] + player_height:
        speed[1] = -speed[1]

    # game over
    if ball_position[1] > 630:
        print("GAME OVER :(")
        exit()
    
    pygame.display.update()
    clock.tick(FPS)
