from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.up()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        
        self.goto(position)


    # Paddle movement functions
    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
