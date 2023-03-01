import turtle

timmy = turtle.Turtle()
print(turtle.screensize())

start = 0
while start <= turtle.window_width():

    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    start += 10


screen = turtle.Screen()
screen.exitonclick()