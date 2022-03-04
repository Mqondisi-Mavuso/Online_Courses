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

    def create_snake(self):
        # creating the body of the snake
        for location in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(location)
            self.segments.append(snake)

    def move(self):
        for seg_num in range(len(STARTING_POSITIONS) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() == 0.0:
            self.segments[0].left(90.0)
        elif self.segments[0].heading() == 180.0:
            self.segments[0].right(90.0)
        else:
            self.segments[0].foward(0)

    def down(self):
        if self.segments[0].heading() == 0.0:
            self.segments[0].right(90.0)
        elif self.segments[0].heading() == 180.0:
            self.segments[0].left(90.0)
        else:
            self.segments[0].foward(0)

    def left(self):
        if self.segments[0].heading() == 90.0:
            self.segments[0].left(90.0)
        elif self.segments[0].heading() == 270.0:
            self.segments[0].right(90.0)
        else:
            self.segments[0].foward(0)

    def right(self):
        if self.segments[0].heading() == 90.0:
            self.segments[0].right(90.0)
        elif self.segments[0].heading() == 270.0:
            self.segments[0].left(90.0)
        else:
            self.segments[0].foward(0)
