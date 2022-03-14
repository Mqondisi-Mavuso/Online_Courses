from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        """
        Default constructor, constructs the object during it's declaration
        """
        super().__init__()
        self.score = 0
        with open("data.txt") as FILE:
            self.high_score = int(FILE.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        """
        Makes the turtle to write the score board on the top part of the screen
        :return:
        """
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # opening the file (relative file path) and writing the new score onto it
            # with open("../../../../data.txt", mode="w") as FILE:
            #     pass
            with open("data.txt", mode="w") as FILE:
                FILE.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()

    def increase_score(self):
        """
        Increment the score whenever the snake ate the food and call the update the score board function
        :return:
        """
        self.score += 1
        self.update_score_board()


