from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "purple", "yellow", "black"]
y_coor = [-100, -50, 0, 50, 100]
all_turtle = []
for turtle in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle])
    tim.goto(x=-230, y=y_coor[turtle])
    all_turtle.append(tim)

is_race = True
while is_race:
    for t in all_turtle:
        distance = random.randint(0, 9)
        t.forward(distance)

    if t.xcor() > 230:
        is_race = False


screen.exitonclick()
