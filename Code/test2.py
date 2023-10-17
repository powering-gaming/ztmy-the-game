import pygame
from settings import *
from debug import debug

pygame.init()

clock = pygame.time.Clock()
clock.tick(FPS)

# create window
screen = pygame.display.set_mode((resX, resY))
pygame.display.set_caption("prototype testing")

# square parameters
square_size = 50
square_x = (resX - square_size) // 2
square_y = (resY - square_size) // 2
playerGravity = 0
playerSpeed = 0.3
groundCheck = False

#obstacle parameters
obsSizeX = 100
obsSizeY = 50
obsX = resX * 3/4 - obsSizeX / 2
obsY = resY * 3/4 - obsSizeY / 2


# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with colour
    screen.fill((255, 255, 255))

    #floor
    if square_y + square_size > resY:
        groundCheck = True
    else:
        groundCheck = False

    if groundCheck == True:
        square_y = resY - square_size

    # Move the square
    keys = pygame.key.get_pressed()

    if square_x > 0:
        if keys[kLeft]:
            square_x -= playerSpeed
        
    if square_x + square_size < resX:
        if keys[kRight]:
            square_x += playerSpeed

    if keys[kJump] and groundCheck:
        playerGravity = -0.5
    
    
            
    playerGravity += 0.0005
    square_y += playerGravity

    # Draw the squares on the window
    pygame.draw.rect(screen, (0, 0, 0), (square_x, square_y, square_size, square_size))
    pygame.draw.rect(screen, (255, 0, 0), (obsX, obsY, obsSizeX, obsSizeY))
    pygame.display.update()

