from turtle import Turtle, Screen
import random

# List of named colors from the Tcl/Tk color set
colors = [
    'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'white',
    'orange', 'purple', 'brown', 'pink', 'gray', 'gold', 'silver', 'navy',
    'skyblue', 'lime', 'turquoise', 'violet', 'indigo', 'maroon'
]

direction = ['forward','backward','right','left']
distance = 25
angle = 90
should_continue = True
tim = Turtle()
tim.speed("fastest")
tim.pensize(10)

while should_continue:
#pick random direction
    random_direction = random.choice(direction)
    random_color = random.choice(colors)
    tim.color(random_color) 
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
