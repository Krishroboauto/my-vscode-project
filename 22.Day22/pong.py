from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import random
import time

#create the screen
crt = Screen()
crt.setup(width = 800,height = 600)
crt.bgcolor("black")
crt.title("Pong")
crt.tracer(0)

paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))

Ball_mid = Ball()

# Listen to keyboard input
crt.listen()
crt.onkey(paddle_r.move_up, "Up")
crt.onkey(paddle_r.move_down, "Down")
crt.onkey(paddle_l.move_up,"w")
crt.onkey(paddle_l.move_down,"s")


game_on = True

while game_on:
    crt.update()
    time.sleep(0.05)
    Ball_mid.move()

    if Ball_mid.ycor() > 280  or Ball_mid.ycor() < -280:
        Ball_mid.bounce_y()

    if Ball_mid.distance(paddle_r) < 50 and Ball_mid.xcor() > 340:
        print("collison")


crt.exitonclick()

