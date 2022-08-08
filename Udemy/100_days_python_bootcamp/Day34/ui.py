from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#0C7B93"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain                 # Used to tap into the quiz_brain class
        self.window = Tk()
        self.window.title("Trivier")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # this is for the front part of the flash card
        self.canvas = Canvas(width=600, height=550)
        self.canvas.config(highlightthickness=0, bg="#D3E0EA")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # self.tria_question = question_data.["question"]
        self.trivial_question = self.canvas.create_text(
            300,
            250,
            width=450,
            text="Questions will be here",
            font=("Ariel", 20, "italic"), fill=THEME_COLOR
        )

        # score text
        self.score_text = Label(self.window,
                                text="Score: 0",
                                font=("Courier", 14),
                                bg=THEME_COLOR, fg="white"
                                )
        self.score_text.grid(row=0, column=1)

        # True button
        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_image,
                                     highlightthickness=0, bg=THEME_COLOR, command=self.correct)
        self.correct_button.grid(row=2, column=0)

        # False button
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, bg=THEME_COLOR, command=self.wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    # This brings up the next question from the quiz_brain
    def get_next_question(self):
        self.canvas.configure(bg="#D3E0EA")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.trivial_question, text=q_text)
        else:
            self.canvas.itemconfig(self.trivial_question, text="You've reached the end of the quiz!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, isright):
        if isright:
            self.canvas.configure(bg="Green")                   # for changing the background of the canvas
        else:
            self.canvas.configure(bg="Red")
        self.window.after(1000, self.get_next_question)
