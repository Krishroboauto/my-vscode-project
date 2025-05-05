from turtle import Turtle, Screen,colormode
import random

# List of named colors from the Tcl/Tk color set




direction = ['forward','backward','right','left']
distance = 25
angle = 90
should_continue = True
tim = Turtle()
tim.speed("fastest")
tim.pensize(10)
colormode(255)



while should_continue:
#pick random direction
    random_direction = random.choice(direction)
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    tim.color(r,g,b) 
    if random_direction == 'forward':
        tim.forward(distance)
    elif random_direction == 'backward':
        tim.backward(distance)
    elif random_direction == 'right':    
        tim.right(angle)
        tim.forward(distance)
    elif random_direction == 'left':
        tim.left(angle)
        tim.forward(distance)


screen = Screen()
screen.exitonclick()
