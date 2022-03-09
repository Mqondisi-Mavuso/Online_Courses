from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        """
        Default constructor that will create the paddles
        :param location: integer that will determine whether the paddle will be on the left or right
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=None)
        self.penup()
        self.goto(location)

    def go_up(self):
        """
        Makes the paddle go up
        :return:
        """
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
