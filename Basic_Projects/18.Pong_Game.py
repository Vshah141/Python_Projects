from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from pongscore import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.screensize(800, 600)
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball=Ball()
score=Scoreboard()
screen.listen()
screen.onkeypress(paddle1.goup, "Up")
screen.onkeypress(paddle1.godown, "Down")
screen.onkeypress(paddle2.goup, "w")
screen.onkeypress(paddle2.godown, "a")


game_is_on = True

while game_is_on:
    time.sleep(ball.sec)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320  or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() <-380:
        ball.reset_position()
        score.r_point()
        




screen.exitonclick()
