from turtle import Turtle

STARTING_POSITION = (0, -280)   # The cars will start on the right side of the screen
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """
        default constructor that inherit the attributes and methods of the Turtle class
        """
        super().__init__()
        self.shape("turtle")
        self.color("magenta")
        self.left(90)
        self.penup()
        self.reset_player()

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)
