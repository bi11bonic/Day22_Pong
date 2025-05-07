from turtle import Turtle
#TODO: 8 - Keep score

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.write(self.score, font=('Arial', 25, 'bold'))
        self.update_score()

    def update_score(self):
        self.clear()

        self.write(self.score, font=('Arial', 25, 'bold'))

    def score_a_point(self):
        self.score += 1
        self.update_score()

