from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))
        self.up()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))
    
