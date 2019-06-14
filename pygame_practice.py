"""

title: pygame_practice
author: Brandon
date: 2019-06-14 09:48
"""

import pygame
# initalize game machine
pygame.init()


# Set the height and width of the screen
size = (750, 750)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
YELLOW = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
brown = (210, 105, 30)
tan = (245, 245, 220)
pi = 3.14159265
orange = (255, 165, 0)
pygame.display.set_caption("First Pygame")


done = False
clock = pygame.time.Clock()

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

ball_pos = 1
ball_change = 10


def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, orange, [100 + x, 430 + ball_pos + y, 40, 40])
    pygame.draw.circle(screen, tan, [200 + x, 200 + y], 120)
    pygame.draw.ellipse(screen, brown, [125 + x, 150 + y, 50, 30])
    pygame.draw.ellipse(screen, brown, [225 + x, 150 + y, 50, 30])
    pygame.draw.arc(screen, red, [100 + x, 120 + y, 200, 150], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, red, [100 + x, 120 + y, 200, 150], 3 * pi / 2, 2 * pi, 2)
    pygame.draw.rect(screen, black, [195 + x, 320 + y, 10, 190])
    pygame.draw.line(screen, black, [200 + x, 360 + y], [250 + x, 430 + y], 5)
    pygame.draw.line(screen, black, [200 + x, 360 + y], [150 + x, 430 + y], 5)
    pygame.draw.line(screen, black, [200 + x, 500 + y], [150 + x, 560 + y], 6)
    pygame.draw.line(screen, black, [200 + x, 500 + y], [250 + x, 560 + y], 6)


while not done:
    ball_pos += ball_change

    if ball_pos > 100:
        ball_change -= 5
    if ball_pos < 0:
        ball_change += 5
    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -10
    if keys[pygame.K_RIGHT]:
        x_speed = 10
    if keys[pygame.K_UP]:
        y_speed = -10
    if keys[pygame.K_DOWN]:
        y_speed = 10

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    screen.fill(white)

    draw_stick_figure(screen, x_coord, y_coord)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
