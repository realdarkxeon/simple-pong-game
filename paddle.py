from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_x, starting_y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_x, starting_y)
        self.color("white")
        self.speed("fastest")
    def move_up(self):
        self.setposition(self.xcor(), self.ycor() + 20)
    def move_down(self):
        self.setposition(self.xcor(), self.ycor() - 20)