from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        """
        Default constructor that will create the body of the snake
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # creating the body of the snake
        for location in STARTING_POSITIONS:
            self.add_segment(location)

    def add_segment(self, location):
        """
        Adds a new segment at the specified location
        :param location: Takes the location tuple (x, y)
        :return:
        """
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(location)
        self.segments.append(snake)

    def extend(self):
        """
        Adds another segment at the tail to increase the length of the snake
        :return:
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        This moves each segment starting with the tail to where the segment in front of it is located
        :return:
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 0.0:
            self.head.left(90.0)
        elif self.head.heading() == 180.0:
            self.head.right(90.0)
        else:
            self.head.forward(0)

    def down(self):
        if self.head.heading() == 0.0:
            self.head.right(90.0)
        elif self.head.heading() == 180.0:
            self.head.left(90.0)
        else:
            self.head.forward(0)

    def left(self):
        if self.head.heading() == 90.0:
            self.head.left(90.0)
        elif self.head.heading() == 270.0:
            self.head.right(90.0)
        else:
            self.head.forward(0)

    def right(self):
        if self.head.heading() == 90.0:
            self.head.right(90.0)
        elif self.head.heading() == 270.0:
            self.head.left(90.0)
        else:
            self.head.forward(0)
