from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_countercw():
    tim.left(10)

def move_cw():
    tim.right(10)

def clear_tim():
    tim.up()
    tim.clear()
    tim.home()
    tim.down()



screen.listen()
screen.onkey(key="w",fun =move_forward)
screen.onkey(key="s",fun =move_backward)
screen.onkey(key="a",fun =move_countercw)
screen.onkey(key="d",fun =move_cw)
screen.onkey(key="c",fun =clear_tim)
screen.exitonclick()