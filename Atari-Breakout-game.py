import os
import sys

import pygame

from pygame.locals import *

pygame.init()

size = width, height = (1000, 600)
icon = pygame.image.load(os.path.join('Images', 'logo.jpg'))
pygame.display.set_icon(icon)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Breakout')

clock = pygame.time.Clock()
run = True

#bouncer in middle of screen
box_width = 100
box_height = 10
x = (size[0] - box_width) / 2 
y = size[1]-30
vel = 18

#targets
target_width = 60
target_heigth = 20




while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 18:
        x -= vel
    if keys[pygame.K_RIGHT] and x < width - 18 - box_width:
        x += vel
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_q]:
        run = False

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, box_width, box_height) )

    #sides
    pygame.draw.rect(window, (230, 230, 230), (0, 0, width, 16))
    pygame.draw.rect(window, (230, 230, 230), (0, 0, 16, height))
    pygame.draw.rect(window, (230, 230, 230), (width, 0, -16, height))

    pygame.display.update()

pygame.quit()
