from turtle import Turtle

#TODO: 2 - Create and move paddle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=.4, stretch_len=4)
        self.color("white")
        self.penup()
        self.goto(position)

    def p_paddle(self):
        self.penup()
        self.goto(x=380, y=0)

    def c_paddle(self):
        self.penup()
        self.goto(x=-380, y=0)

    # TODO: 3 - Create computer paddle



    def up(self):
        if  self.ycor() < 280:
            self.penup()
            self.setheading(90)
            self.forward(20)
        else:
            pass

    def down(self):
        if  self.ycor() > -280:
            self.penup()
            self.setheading(90)
            self.backward(20)
        else:
            pass

    # def comp_move(self):
    #     self.comp_paddle.speed("fast")
    #     self.comp_paddle.penup()
    #     for _ in range(15):
    #         self.comp_paddle.forward(20)
    #     while self.is_game_on:
    #         if self.comp_paddle.ycor() > 270:
    #             for _ in range(31):
    #                 self.comp_paddle.backward(20)
    #         elif self.comp_paddle.ycor() < -270:
    #             for _ in range(31):
    #                 self.comp_paddle.forward(20)
