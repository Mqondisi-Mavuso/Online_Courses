from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = (random.randint(-550, 550), random.randint(-550, 550))


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()

    def create_cars(self):
        for _ in range(1, 30):
            self.generate_cars()

    def generate_cars(self):
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.left(270)
        car.turtlesize(stretch_wid=2.5, stretch_len=1, outline=None)
        car.goto(POSITIONS)
