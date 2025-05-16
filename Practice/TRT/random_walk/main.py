import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


setheading_angle = [0,90,180,270]
screen.colormode(255)
tim.pensize(10)

for _ in range(0,100):
    angle_choice = random.choice(setheading_angle)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.color(r,g,b)
    tim.setheading(angle_choice)
    tim.forward(10)

screen.exitonclick()
