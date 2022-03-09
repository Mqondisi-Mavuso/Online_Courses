from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        """
        default constructor, it also inherits all the attributes of the Turtle
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        """
        This writes the score board at the top middle part of the screen
        :return:
        """
        self.clear()
        self.goto(-100, 150)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 150)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def l_point(self):
        """
        Incrementing the left paddle score everytime the opponent missed the ball
        :return:
        """
        self.l_score += 1
        self.update_score()

    def r_point(self):
        """
        For incrementing the right paddle score everytime their opponent missed the ball
        :return:
        """
        self.r_score += 1
        self.update_score()