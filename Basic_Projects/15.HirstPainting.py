import turtle as turtle_mode
from turtle import Screen
import random
turtle_mode.colormode(255)
t = turtle_mode.Turtle()
color_list = [(202, 164, 109), (238, 240, 245),
              (150, 75, 49), (223, 201, 135), (52, 93, 124)]


screen = turtle_mode.Screen()
t.penup()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
for _ in range(1, 101):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if _ % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen.exitonclick()
