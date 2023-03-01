import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)


def shape(number_of_side):
    for _ in range(number_of_side):
        timmy.pencolor(r, g, b)
        timmy.right(360 / x)
        timmy.forward(100)


start = 3
for x in range(3, 11):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    shape(x)


screen = turtle.Screen()
screen.exitonclick()