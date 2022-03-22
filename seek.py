"""Seek behaviour in Pygame"""

import pygame
import numpy as np
import math

WIDTH,HEIGHT = 700,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Seeker():
    def __init__(self,x,y):
        super().__init__()
        self.pos=np.array([x,y])
        self.vel=np.array([0,0])
        self.acc=np.array([0,0])
        self.max_speed=0.1

    def Draw(self):
        #pygame.draw.polygon(screen, (0,255,255), ((self.pos),(self.pos+(8,-20)),(self.pos+(18,0))))
        pygame.draw.circle(screen, (0,255,255), self.pos, 10)
    
    def Update(self):
        self.vel = np.add(self.vel, self.acc)
        self.pos = np.subtract(self.pos, self.vel)
        self.acc = np.multiply(self.acc,[0,0])

    def Apply(self,force):
        self.acc = np.add(self.acc,force)

    def Seek(self,target):
        desired_vel = self.pos - target
        desired_vel = desired_vel/math.sqrt(desired_vel[0]*desired_vel[0]+desired_vel[1]*desired_vel[1])
        desired_vel = desired_vel * self.max_speed
        
        steering_vel = desired_vel - self.vel
        self.Apply(steering_vel)

def Snitch(pos):
    pygame.draw.circle(screen, (255,215,0), pos,10)

pygame.init()

agents=[]
for i in range(20):
    agents.append(Seeker(i*100,i*100))

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get target position
    target_pos= np.array(pygame.mouse.get_pos())

    Snitch(target_pos)
    for agent in agents:
        agent.Seek(target_pos)
        agent.Update()
        agent.Draw()

    

    pygame.display.update()
    #pygame.time.Clock().tick(30)