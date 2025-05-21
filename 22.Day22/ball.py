from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")  
        self.x_move = 5
        self.y_move = 5     


    # Paddle movement functions
    def move(self):
        x = self.xcor()
        y = self.ycor()
        x += self.x_move
        y += self.y_move
        self.goto(x,y)
    
    def bounce_y(self):
        self.y_move = self.y_move * -1
    
    def bounce_x(self):
        self.x_move = self.x_move * -1

   