from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.3


class CarManager(Turtle):
    def __init__(self):
        """
        default constructor that inherits the Turtle class
        """
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)             #make the car face the left
            car.turtlesize(stretch_wid=1, stretch_len=2.5, outline=None)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
