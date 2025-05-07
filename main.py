
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import random

#TODO: 1 - Create Screen
background = Screen()
background.setup(width = 800, height= 600)
background.bgcolor("black")
background.title("Pong")

# Eliminates animation of the turtles on game start
background.tracer(0)

game_is_on = True

# Creates dashed line in center
center_dash = Turtle()
center_dash.speed("fastest")
center_dash.goto(x=0, y= -300)
center_dash.pensize(width=5)
center_dash.pencolor("white")
center_dash.setheading(90)
y = -300

while y < 300:
    center_dash.pendown()
    center_dash.forward(20)
    center_dash.penup()
    center_dash.forward(20)
    y += 40
center_dash.hideturtle()


# Initiate the score and scorekeeping, tuple is the position of the numbers
p_score = Score((200, 250))
c_score = Score((-200, 250))


# initiate the paddles and the ball, tuple is the starting position of the paddles
p_paddle = Paddle((380, 0))

c_paddle = Paddle((-380, 0))

ball = Ball()



# Make paddles respond to keystrokes
background.listen()
background.onkey(p_paddle.up, "Up")
background.onkey(p_paddle.down, "Down")
background.onkey(c_paddle.up, "w")
background.onkey(c_paddle.down, "s")

# Set animation back to regular mode
background.tracer(1)

while game_is_on:
    # Checks scores to see if the game continues
    # print(f"p_score = {p_score.score}, c_score = {c_score.score}")
    if p_score.score >= 5 or c_score.score >= 5:

        game_is_on = False


    background.update()

    # TODO: 5 - Detect collision and make it bounce
    if -280 < ball.ycor() or ball.ycor() < 280 and -400 < ball.xcor() or ball.xcor() < 400:

        ball.ball_move()
        if -280 > ball.ycor() or ball.ycor() > 280:
            background.tracer(0)
            ball.bounce()
            background.tracer(1)
    # print(ball.position())

        # TODO: 6 - Detect collision with paddle
    # Collision detection

        if ball.distance(p_paddle) < 50 and ball.xcor() > 360:
            # print(ball.heading())
            background.tracer(0)
            ball.setheading(180 - (ball.heading() + random.randint(1,10)))
            # print(ball.heading())
            background.tracer(1)
            ball.ball_move()
            ball.ball_move()
        if ball.distance(c_paddle) < 50 and ball.xcor() < -360:
            # print(ball.heading())
            background.tracer(0)
            if 90 < ball.heading() < 180:
                ball.setheading(180 - ball.heading() + random.randint(1,10))
                background.tracer(1)
                ball.ball_move()
                ball.ball_move()
            elif 180 < ball.heading() < 270:
                ball.setheading(360 - (ball.heading() - 180 + random.randint(1,10)))
                # ball.forward(51)
                background.tracer(1)
                ball.ball_move()
                ball.ball_move()

        # TODO: 7 - Detect when paddle misses
        elif ball.xcor() > 400:
            ball.teleport(0,0)
            ball.ball_heading()
            c_score.score_a_point()
            c_score.update_score()
            ball.ball_heading()

        elif ball.xcor() < -400:
            ball.teleport(0, 0)
            ball.ball_heading()
            p_score.score_a_point()
            p_score.update_score()
            ball.ball_heading()

if game_is_on is False:
    ball.teleport(0, 0)


background.exitonclick()