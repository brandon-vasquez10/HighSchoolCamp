"""

title: pygame_practice
author: Brandon
date: 2019-06-14 09:48
"""

import pygame
#initalize game machine
pygame.init()


# Set the height and width of the screen
size = (750, 750)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")


done = False
clock = pygame.time.Clock()


while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    white = (255, 255, 255)
    YELLOW = (255, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    brown = (210, 105, 30)
    tan = (245, 245, 220)
    pi = 3.14159265

    screen.fill(white)
    pygame.draw.circle(screen, tan, [200, 200], 120)
    pygame.draw.ellipse(screen, brown, [125, 150, 50, 30])
    pygame.draw.ellipse(screen, brown, [225, 150, 50, 30])
    pygame.draw.arc(screen, red, [100, 120, 200, 150], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, red, [100, 120, 200, 150], 3 * pi / 2, 2 * pi, 2)
    pygame.draw.rect(screen, black, [195, 320, 10, 190])
    pygame.draw.line(screen, black, [200, 360], [250, 430], 5)
    pygame.draw.line(screen, black, [200, 360], [150, 430], 5)
    pygame.draw.line(screen, black, [200, 500], [150, 560], 6)
    pygame.draw.line(screen, black, [200, 500], [250, 560], 6)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
