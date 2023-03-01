import random
import turtle


timmy = turtle.Turtle()
turtle.colormode(255)
timmy.pensize(15)
timmy.speed("fastest")


def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple

while True:
    angle = random.choice([0, 90, 180, 270])
    colour = random_colours()
    timmy.pencolor(colour)
    timmy.forward(30)
    timmy.setheading(angle)


screen = turtle.Screen()
screen.exitonclick()