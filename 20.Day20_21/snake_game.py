from turtle import Turtle, Screen
from food import Food
import random
import time
from snake import Snake
from score_board import ScoreBoard

screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    #detect collision with tail
    for segment in snake.segments[1:]:  # Skip the head itself
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

    
        


screen.exitonclick()


