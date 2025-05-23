from turtle import Turtle, Screen
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] 

    def add_segment(self,position):
        tim_1 = Turtle()
        tim_1.shape("square")
        tim_1.color("white")
        tim_1.up()
        tim_1.goto(position)
        #tim_1.speed("slowest")
        self.segments.append(tim_1)

    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):

            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)    


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    


