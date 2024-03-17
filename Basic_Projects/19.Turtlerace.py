import time
from turtle import Turtle, Screen
from player import Playered
from cars import Cars
from turtlescore import Scoreboard

screen = Screen()
screen.screensize(600, 600)
screen.title("Turtle Race")
screen.bgcolor("white")
screen.tracer(0)


player = Playered()
car = Cars()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.goup, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createcar()
    car.move()

    for each in car.allcars:
        if each.distance(player) < 20:
            game_is_on = False
            score.gameover()

    if player.atfinishline():
        player.start()
        score.inclevel()
        car.levelup()


screen.exitonclick()
