# day 18 of 100 turtle drawing
from turtle import Turtle
from turtle import Screen
from random import randint
# import colorgram

# extracting the colors from the hirst image
# colors = colorgram.extract('hirst.jpg', 50)

# rgb_colors = []
# cleaning the data and putting it in a list we can easily use
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(229, 249, 73), (229, 237, 253), (67, 252, 194),
              (17, 184, 82), (19, 15, 96), (218, 153, 94), (74, 37, 23), (94, 1, 56), (59, 4, 180), (247, 102, 203),
              (28, 245, 41), (248, 21, 135), (168, 3, 123), (6, 99, 40), (100, 179, 5), (50, 15, 253), (106, 172, 243),
              (172, 92, 13), (11, 92, 180), (64, 114, 247), (183, 183, 250), (183, 2, 1), (249, 21, 18), (53, 98, 1),
              (76, 248, 252), (4, 181, 187), (19, 151, 58), (172, 47, 128), (2, 98, 101), (237, 161, 212),
              (191, 11, 145), (4, 74, 28), (252, 11, 7), (244, 162, 157), (202, 253, 0), (15, 251, 198)
              ]
neo = Turtle()
neo.hideturtle()
neo.speed("fastest")
neo.shape("turtle")
screen = Screen()
screen.colormode(255)
neo.penup()
neo.setposition(-200, -200)
x_origin= neo.xcor()
y_origin = neo.ycor()

# print(type(x_origin))
for p in range(10):
    for pos in range(10):
        neo.dot(40, color_list[randint(0, len(color_list)) - 1])
        neo.penup()
        neo.forward(50)
    neo.penup()
    neo.setposition(x_origin, y_origin + 50)
    y_origin = neo.ycor()


# this is for adding the spirograph of top of the art
neo.penup()
neo.setposition(25, 25)
gap_size = 5
neo.pendown()
for i in range(int(360/gap_size)):
    neo.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    neo.circle(100)
    neo.setheading(neo.heading() + gap_size)

screen.exitonclick()
