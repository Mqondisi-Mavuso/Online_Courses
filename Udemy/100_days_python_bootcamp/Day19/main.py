# Day 19 of 100 python bootcamp
# Turtle graphics, turtle race game

from turtle import Turtle, Screen
from random import randint

colors = ["lime", "pink", "magenta", "orange", "yellow", "grey"]
y_coordinates = [-100, -50, 0, 50, 100, 151]
screen = Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title = "Make your bet" , prompt = f"Which turtle is going to win? ({colors}): ")
turtle_list = []
race_on = False

# This is for generating the different turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x =-230, y = y_coordinates[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    race_on = True

winner = ""

# For the race
while race_on:
    for turtle in turtle_list:
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 250:
            race_on = False
            winner = list(turtle.color())[1]
if winner == user_bet:
    print(f"Your {winner} turtle won!")
else:
    print(f"You lost, the winner is the {winner} turtle")


# def move_forward():
#   mqo.forward(100)
#
# def move_backwards():
#   mqo.backward(100)
#
# def move_anti_clockwise():
#   mqo.left(45)
#
# def move_clockwise():
#   mqo.right(45)
#
# def clear():
#   mqo.clear()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backwards, "b")
# screen.onkey(move_anti_clockwise, "a")
# screen.onkey(move_clockwise, "d")
# screen.onkey(clear, "c")

screen.exitonclick()
