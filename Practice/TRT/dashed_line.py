from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.up()
tim.backward(25)
tim.down()

for i in range(0,25):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()


screen.exitonclick()
