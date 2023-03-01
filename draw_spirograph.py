import random
import turtle


timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")


def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple


start_angle = 10
while start_angle <= 360:
    timmy.circle(120, 360)
    colour = random_colours()
    timmy.pencolor(colour)
    timmy.setheading(start_angle)
    start_angle += 5


screen = turtle.Screen()
screen.exitonclick()