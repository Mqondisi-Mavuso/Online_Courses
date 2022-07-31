from tkinter import *
from data import question_data
import requests

THEME_COLOR = "#0C7B93"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Trivier")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        # this is for the front part of the flash card
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(highlightthickness=0, bg="#D3E0EA")
        self.canvas.grid(column=0, row=1, columnspan=2)
        # self.tria_question = question_data.["question"]
        # self.trivial_question = self.canvas.create_text(400, 150, text=self.tria_question, font=("Ariel", 5, "italic"))

        # score text
        self.GUI_text = Label(self.window, text="Score: 0", font=("Courier", 14), bg=THEME_COLOR)
        self.GUI_text.grid(row=0, column=1)

        # True button
        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_image, highlightthickness=0, bg=THEME_COLOR)
        self.correct_button.grid(row=2, column=0)

        # False button
        self.wrong_image = PhotoImage(file="images/false.png")
        self.correct_button = Button(image=self.wrong_image, highlightthickness=0, bg=THEME_COLOR)
        self.correct_button.grid(row=2, column=1)

        self.window.mainloop()
