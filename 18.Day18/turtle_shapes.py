from turtle import Turtle, Screen
import random

# List of named colors from the Tcl/Tk color set
colors = [
    'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'white',
    'orange', 'purple', 'brown', 'pink', 'gray', 'gold', 'silver', 'navy',
    'skyblue', 'lime', 'turquoise', 'violet', 'indigo', 'maroon'
]

#draw triange
tim = Turtle()

n_start =  3 #start  with trainge
n_end = 13      # decagon


for shape in range(n_start,n_end):
    random_color = random.choice(colors)
    tim.color(random_color)
#triange - 3 times
    for _ in range(0,shape):
        tim.forward(100)
        tim.right(360/shape)

'''
random_color = random.choice(colors)
tim.color(random_color)
#square
for _ in range(0,4):
    tim.forward(100)
    tim.right(90)

random_color = random.choice(colors)
tim.color(random_color)
#pentagon 
for _ in range(0,5):
    tim.forward(100)
    tim.right(72)

random_color = random.choice(colors)
tim.color(random_color)
#Hexagon
for _ in range(0,6):
    tim.forward(100)
    tim.right(60)

random_color = random.choice(colors)
tim.color(random_color)
#Heptagon
for _ in range(0,7):
    tim.forward(100)
    tim.right(360/7)

random_color = random.choice(colors)
tim.color(random_color)
#Octagon
for _ in range(0,8):
    tim.forward(100)
    tim.right(360/8)

random_color = random.choice(colors)
tim.color(random_color)
#nanogon
for _ in range(0,9):
    tim.forward(100)
    tim.right(360/9)

'''





screen = Screen()
screen.exitonclick()
