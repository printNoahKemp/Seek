import turtle
import random
import math

def Walker(instruction):
    turtle.hideturtle()
    if instruction == 0:
        turtle.forward(3)
    elif instruction == 1:
        turtle.right(math.pi*instruction*10)
        turtle.forward(3)
    elif instruction == 2:
        turtle.left(math.pi*instruction*10)
        turtle.forward(3)
    elif instruction == 3:
        turtle.backward(3)
def Setup():
    running = True
    while running:
        rand_instruc = random.randrange(0,4)
        Walker(rand_instruc)
Setup()