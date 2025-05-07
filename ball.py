from turtle import Turtle, Screen
import random

#TODO: 4 - Create ball and make it move

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("slowest")
        self.color("white")
        self.penup()
        self.head_1 = 0
        self.heading_new = 0



    def ball_heading(self):

        self.head_1 = random.randint(0, 90)
        # print(self.head_1)
        if self.head_1 < 45:
            self.setheading(self.head_1)

        elif self.head_1 >= 45:
            self.setheading(360 - (self.head_1 - 45))


    def ball_move(self):
        self.forward(10)



    def bounce(self):
        self.heading_new = 360 - self.heading()
        self.setheading(self.heading_new)
        self.forward(20)
        # self.forward(20)
        self.ball_move()
