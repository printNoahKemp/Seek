from turtle import st
import pygame
import numpy as np
import math

WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN = (0,255,255)
GOLD = (255,215,0)

WIDTH,HEIGHT = 700,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Seeker():
    def __init__(self,x,y):
        super().__init__()
        self.pos=np.array([x,y])
        self.vel=np.array([0,0])
        self.acc=np.array([0,0])
        self.max_speed=0.1
        self.max_force=0.1

    def Draw(self):
        pygame.draw.circle(screen, CYAN, self.pos, 10)
    
    def Update(self):
        self.vel=np.add(self.vel,self.acc)
        self.vel = np.clip(self.vel,0,self.max_speed)
        self.pos=np.subtract(self.pos,self.vel)
        self.acc = np.array([0,0])

    def Apply(self,force):
        self.acc = np.add(self.acc,force)

    def Seek(self,target):
        target = np.array(target)
        desired = np.subtract(target, self.pos)

        desired_hat=desired/np.linalg.norm(desired)
        desired = desired_hat*self.max_speed

        """desired = np.linalg.norm(desired)
        desired = np.multiply(desired,self.max_speed)"""
        desired = np.subtract(desired,self.vel)

        steer = np.clip(desired,0,self.max_force)
        self.Apply(steer)

        # normalized_pos = (self.pos-target)/(np.linalg.norm(self.pos-target))
        # desired_velocity = normalized_pos*self.max_speed
        # steering = desired_velocity - self.vel
        # print("###Seek###")
        # print("norm_pos:{0}|des_vel:{1}|steer:{2}".format(normalized_pos,desired_velocity,steering))
        #self.Apply(steering)
    
    def Slow(self):
        if self.max_speed>0:
            self.max_speed -= 1

def Snitch(pos):
    pygame.draw.circle(screen, GOLD, pos,10)

pygame.init()
seeker=Seeker(350.0,200.0)

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get target position
    target_pos= np.array(pygame.mouse.get_pos())
    #Draw seeker and snitch
    Snitch(target_pos)
    #Draw and update seeker
    seeker.Seek(target_pos)
    seeker.Update()
    seeker.Draw()

    pygame.display.update()
    #pygame.time.Clock().tick(5)