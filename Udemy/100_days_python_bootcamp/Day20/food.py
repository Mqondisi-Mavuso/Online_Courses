from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        """
        default constructor that initialize the "food" turtle, it inherits the Turtle class
        """
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # Making the turtle size smaller than normal
        self.color("lime")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Makes the food appear in another random place of the screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
