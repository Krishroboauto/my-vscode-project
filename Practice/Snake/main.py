from turtle import  Screen
from snake_body import SnakeBody
import random
import time
from food import Food
from scoreboard import ScoreBoard
#from timer import TimerBoard

USE_TIMER = False

screen = Screen()
screen.screensize(canvwidth= 600, canvheight= 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = SnakeBody()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")


if USE_TIMER:
    from timer import TimerBoard
    # Start time tracking
    timer = TimerBoard()
    start_time = time.time()
    last_timer_update = start_time  

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if USE_TIMER:
        current_time = time.time()
        if current_time - last_timer_update >= 1:
            timer.countdown()
            last_timer_update = current_time

        if timer.remaining_seconds <= 0:
            game_on = False
            score.game_over()

    # detect collosion with food
    if snake.head.distance(food) < 10:
        food.regen_food()
        score.increase_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 470 or snake.head.xcor() < -470 or snake.head.ycor() > 400 or snake.head.ycor() < -390:
        game_on = False
        score.game_over()
    
    #detect collision with tail
    for segment in snake.turtles[1:]:  # Skip index 0 (the head)
        if snake.head.distance(segment) < 5:
            game_on = False
            score.game_over()




screen.exitonclick()
