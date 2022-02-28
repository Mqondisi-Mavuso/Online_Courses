from turtle import Turtle
from turtle import Screen
import random as r
neo = Turtle()
screen = Screen()
neo.shape("turtle")
neo.color("medium violet red")

neo.pensize(3)
neo.speed(0)
screen.colormode(255)
# This is for the polygon drawings
# for i in range(3, 10 + 1):
#     screen.colormode(255)
#     neo.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
#     for side in range(1, i + 1):
#         neo.forward(100)
#         neo.left(360/i)


# This is for the random walk drawing
# directions = [0, 90, 180, 270]
#
# for i in range(200):
#     screen.colormode(255)
#     neo.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
#     neo.forward(30)
#     neo.setheading(r.choice(directions))

# For printing the spirograph
gap_size = 5
for i in range(int(360/gap_size)):
    neo.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
    neo.circle(100)
    neo.setheading(neo.heading() + gap_size)

screen.exitonclick()
