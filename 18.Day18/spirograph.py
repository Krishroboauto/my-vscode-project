from turtle import Turtle, Screen,colormode
import random

# List of named colors from the Tcl/Tk color set


tim = Turtle()
tim.speed("fastest")
colormode(255)

radius = 100
total_circles = 100

for i in range(1,total_circles+1):
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    tim.color(r,g,b) 
    tim.circle(radius)
    tim.left(360/total_circles)

screen = Screen()
screen.exitonclick()
