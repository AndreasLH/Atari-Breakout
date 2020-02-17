import os, sys
import pygame
from pygame.locals import *

pygame.init()

size = width, height = (500, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Breakout')

x = 50
y = 50
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_q]:
        run = False

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height) )
    pygame.display.update()

pygame.quit()
sys.exit()


