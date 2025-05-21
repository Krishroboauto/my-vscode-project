from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class SnakeBody:

    def __init__(self):
        self.turtles = []
        self.num_segments = 3
        self.snake()
        self.head = self.turtles[0]
        #self.snake_move()
    
    def snake(self):
        for i in range(self.num_segments):
            position = (-10 * i, 0)
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.up()
        tim.color("white")
        tim.shapesize(stretch_wid=0.5, stretch_len=0.5)
        tim.goto(position)
        self.turtles.append(tim)

    def extend(self):
        # Add segment at the position of the last segment (tail)
        tail = self.turtles[-1]
        self.add_segment(tail.position())
    
    def snake_move(self):
        for teller in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[teller - 1].xcor()
            new_y = self.turtles[teller - 1].ycor()
            self.turtles[teller].goto(new_x, new_y)
        self.head.forward(10)   


    def move_up(self):
        if self.head.heading() != DOWN:   
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:   
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:   
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:   
            self.head.setheading(RIGHT)