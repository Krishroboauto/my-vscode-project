from turtle import Turtle, Screen

tim = Turtle()

#move by 50 diemnsions to left
tim.up()
tim.backward(100)

for _ in range(0,25):
    tim.down()
    tim.forward(10)
    tim.up()
    tim.forward(10)

screen = Screen()

screen.exitonclick()
