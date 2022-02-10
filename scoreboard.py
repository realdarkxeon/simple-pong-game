from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.display()
    def left_increment(self):
        self.left_score += 1
        self.display()
    def right_increment(self):
        self.right_score += 1
        self.display()
    def display(self):
        self.goto(-50, 200)
        self.write(self.left_score, align="center", font=("Courier", 40, "bold"))
        self.goto(50, 200)
        self.write(self.right_score, align="center", font=("Courier", 40, "bold"))
        self.goto(0, 200)
        self.write(":", align="center", font=("Courier", 40, "normal"))