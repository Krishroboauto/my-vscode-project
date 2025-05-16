from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500,height = 400)
colors = ["violet","indigo","blue","green","yellow","orange","red"]
y_positions = [-90,-60,-30,0,30,60,90]
race_on = False

turtles = []

for i in range(7):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.up()  
    tim.goto(x=-230,y=y_positions[i])
    turtles.append(tim)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color from VIBGYOR:")


if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner")            
        
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        









screen.exitonclick()