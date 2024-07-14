import pygame

pygame.init()

# Important variable
X_SIZE = 640
Y_SIZE = 640
FPS = 60
player_x = 300
player_y = 580
ball_x = 345
ball_y = 550
speed = [2, 2]

# set the title, icon and bg
logo_image = pygame.image.load("ping-pong.png")
background_image = pygame.image.load("Background.png")
logo = pygame.display.set_icon(logo_image)
title = pygame.display.set_caption("Pong_Game")

display = pygame.display.set_mode((X_SIZE, Y_SIZE))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.blit(background_image, (0,0))

    # player movement and collision detection
    player = pygame.draw.rect(display, "blue", pygame.Rect(player_x, player_y, 100, 20), width = 3,)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
        if player_x < 0:
            player_x = 0

    if keys[pygame.K_RIGHT]:
        player_x += 5
        if player_x > 540:
            player_x = 540


    # make the ball bounch
    ball = pygame.draw.circle(display, "white", center=[100, 100], radius = 15)
    is_hit = pygame.Rect.colliderect(player, ball)
    
    ball = ball.move(speed)
    if ball.left <= 0 or ball.right >= 540:
        speed[0] = -speed[0] 

    if ball.top <= 0 or is_hit:
        speed[1] = -speed[1]

    pygame.draw.circle(display, "red", center=ball.center, radius=15)

    


    pygame.display.flip()
    clock.tick(FPS)
