'''Autonomous beings'''
'''The nature of code'''
'''Bouncing ball'''

import pygame
import random

HEIGHT=400
WIDTH=700
BLACK=(0,0,0)
WHITE=(255,255,255)

x=10
y=10
x_speed=random.randrange(0,10)/10
y_speed=random.randrange(0,10)/10

screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True

pygame.init()

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x+=x_speed
    y+=y_speed
    if x<0 or x>WIDTH:
        x_speed*=-1
    elif y<0 or y>HEIGHT:
        y_speed*=-1
    

    pygame.draw.circle(screen, WHITE, (x,y), 15)

    pygame.display.update()