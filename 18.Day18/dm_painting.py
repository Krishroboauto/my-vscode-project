from turtle import Turtle, Screen,colormode
import random


color_list = [(194, 170, 11), (172, 79, 35), (57, 89, 148), (231, 221, 81), (221, 222, 3), (110, 172, 209), (146, 67, 85), (213, 159, 83), (207, 74, 116), (33, 127, 102), (82, 97, 207), (225, 126, 166), (210, 73, 56), (28, 186, 213), (41, 56, 117), (76, 157, 78), (50, 56, 64), (149, 211, 178), (130, 212, 235), (88, 65, 34), (83, 54, 29), (34, 67, 66), (132, 184, 163), (33, 78, 77), (220, 173, 198), (177, 185, 218)]


distance = 25
angle = 90
should_continue = True
tim = Turtle()
tim.speed("fastest")
tim.pensize(10)
colormode(255)

tim.up()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.down()


# Draw 10x10 dots
for row in range(10):
    for col in range(10):
        tim.up()
        tim.dot(25, random.choice(color_list))
        tim.forward(40)
        
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(400)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()


screen = Screen()
screen.exitonclick()















