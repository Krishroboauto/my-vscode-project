import random

class Shapes:

    LENGTH = 100
    FULL_ANGLE = 360
    TRIANGLE = 3
    SQUARE = 4
    PENTAGEON = 5
    HEXAGON = 6
    SEPTAGON = 7
    OCTAGON = 8
    NONAGON = 9
    DECAGON = 10

    # List of named colors from the Tcl/Tk color set
    COLORS = [
    'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'white',
    'orange', 'purple', 'brown', 'pink', 'gray', 'gold', 'silver', 'navy',
    'skyblue', 'lime', 'turquoise', 'violet', 'indigo', 'maroon'
    ]



    def __init__(self,turtle):
        self.turtle = turtle
        self.traingle()
        self.square()
        self.pentagon()
        self.hexagon()
    

    def traingle(self):   
        self.turtle.color(random.choice(self.COLORS))     
        for _ in range(0,self.TRIANGLE):
            self.turtle.forward(self.LENGTH)
            self.turtle.right(self.FULL_ANGLE/self.TRIANGLE)

    def square(self):
        self.turtle.color(random.choice(self.COLORS)) 
        for _ in range(0,self.SQUARE):
            self.turtle.forward(self.LENGTH)
            self.turtle.right(self.FULL_ANGLE/self.SQUARE)

    def pentagon(self):
        self.turtle.color(random.choice(self.COLORS)) 
        for _ in range(0,self.PENTAGEON):
            self.turtle.forward(self.LENGTH)
            self.turtle.right(self.FULL_ANGLE/self.PENTAGEON)

    def hexagon(self):
        self.turtle.color(random.choice(self.COLORS)) 
        for _ in range(0,self.HEXAGON):
            self.turtle.forward(self.LENGTH)
            self.turtle.right(self.FULL_ANGLE/self.HEXAGON)
