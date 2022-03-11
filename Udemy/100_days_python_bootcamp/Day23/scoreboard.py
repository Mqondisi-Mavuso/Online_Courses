from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.write(f"Stage: {self.score}", False, align="center", font=FONT)

    def increase_score(self):
        """
        for incrementing the player score
        :return:
        """
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", False, align="center", font=FONT)
