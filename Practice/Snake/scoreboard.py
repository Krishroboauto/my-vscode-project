from turtle import Turtle
import random

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.color("white")
        self.goto(0,380)
        self.hideturtle()
        self.update_score()        

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align = "center", font = ("Arial", 12, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_score()        
        

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))

