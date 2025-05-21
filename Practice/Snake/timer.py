from turtle import Turtle

class TimerBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(200,380)
        self.remaining_seconds = 120
        self.display_timer()

    def display_timer(self):
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.clear()
        self.write(f"Time Left: {minutes:02d}:{seconds:02d}", align="center", font=("Arial", 14, "normal"))

    def countdown(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.display_timer()
