# DAY 31
# flash card project
from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
BACKGROUND_COLOR = "#8CC0DE"

# -------------------------------GET DATA---------------------------------------------#

df = pd.read_csv("data/chinese_words.csv")
my_dict = df.to_dict(orient="records")



def next_card():
    current_card = random.choice(my_dict)
    canvas_front.itemconfig(card_title, text="Chinese (Traditional)")
    canvas_front.itemconfig(card_word, text=current_card["Chinese (Traditional)"])



# -------------------------------UI SETUP---------------------------------------------#
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# this is for the front part of the flash card
canvas_front = Canvas(width=800, height=526)
canvas_front.config(highlightthickness=0, bg=BACKGROUND_COLOR)
front_flash = PhotoImage(file="images/card_front_r.png")
canvas_front.create_image(400, 263, image=front_flash)
canvas_front.grid(column=0, row=0, columnspan=2)
card_title = canvas_front.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas_front.create_text(400, 263, text="", font=("Ariel", 100, "bold"))

# this is for the correct button
correct_image = PhotoImage(file="images/right_2.png")
correct_button = Button(image=correct_image,highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
correct_button.grid(row=1, column=0)

# this is for the wrong button
wrong_image = PhotoImage(file="images/wrong_4.png")
wrong_button = Button(image=wrong_image,highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()
window.mainloop()
