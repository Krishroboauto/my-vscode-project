from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Makes it small like a dot
        self.speed("fastest")  
        self.regen_food() 

    def regen_food(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x, random_y)

