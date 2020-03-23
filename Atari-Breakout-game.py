import os
#import sys

import pygame

#from pygame.locals import *

pygame.init()

size = width, height = (1000, 600)
icon = pygame.image.load(os.path.join('Images', 'logo.jpg'))
pygame.display.set_icon(icon)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Breakout')

clock = pygame.time.Clock()
run = True

#targets
target_width = 60
target_heigth = 20

class Player(object):
    def __init__(self, x, y, box_width, box_height):
        self.x = x
        self.y = y
        self.vel = 30
        self.box_width = 100
        self.box_height = 10

    def draw(self, win):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.box_width, self.box_height) )
        #sides
        pygame.draw.rect(window, (230, 230, 230), (0, 0, width, 16))
        pygame.draw.rect(window, (230, 230, 230), (0, 0, 16, height))
        pygame.draw.rect(window, (230, 230, 230), (width, 0, -16, height))

class Target(Player):
    pass

class Ball(object):
    def __init__(self, x, y, box_width, box_height):
        pass
    def draw(self, win):
        pygame.draw.circle(window, (255, 255, 255), (int(self.x+50), int(self.y-30)), 10)


def drawGame():
    window.fill((0, 0, 0))
    player.draw(window)
    pygame.display.update()
#(size[0] - box_width) / 2, size[1]-30
player = Player((size[0]-50) / 2, size[1]-30, 100, 10)
#main
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 18:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < width - 18 - player.box_width:
        player.x += player.vel
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_q]:
        run = False

    drawGame()

pygame.quit()
