from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """
        default constructor that also inherits the methods and attributes of the Turtle class
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 2
        self.y_move = 2

    def move(self):
        """
        Moves the ball across the screen
        :return:
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        This is for bouncing the ball off the top and bottom walls
        :return:
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Changing the ball's x direction
        :return:
        """
        self.x_move *= -1

    def reset_position(self):
        """
        Resetting the backs to the center if it happened that one of the players missed the ball
        :return:
        """
        self.goto(0, 0)
        self.bounce_x()

