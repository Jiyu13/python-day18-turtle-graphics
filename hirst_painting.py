import random
import colorgram
import turtle

colors = colorgram.extract("image.png", 30)
turtle.colormode(255)

timmy = turtle.Turtle()


color_list = []
for color in colors:
    rgb_colors = color.rgb
    r_color = rgb_colors.r
    g_color = rgb_colors.g
    b_color = rgb_colors.b
    color_list.append((r_color, g_color, b_color))

timmy.speed("fastest")
timmy.hideturtle()
timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    random_color = random.choice(color_list)
    timmy.dot(20, random_color)
    timmy.penup()
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()