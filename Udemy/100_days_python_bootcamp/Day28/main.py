from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    count_down(1 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10 and count_sec % 10 != 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")           # for changing the count on GUI
    if count > 0:
        window.after(1000, count_down, count - 1)       # Count down every second

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer = Label(text="Timer", font=("Times New Roman", 24, "bold"))
timer.config(bg=YELLOW)
timer.config(fg=GREEN)
timer.grid(row=0, column=1)                # This allows the label to be shown on the screen

check_box = Label(text="✔", font=("Times New Roman", 24, "bold"))
check_box.config(bg=YELLOW)
check_box.config(fg=GREEN)
check_box.grid(row=3, column=1)                # This allows the label to be shown on the screen

start_button = Button(text="Start", command=start_timer, highlightthickness=0)     # listens to click from user, click()
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=start_timer, highlightthickness=0)     # listens to click from user
reset_button.grid(row=2, column=2)
window.mainloop()                                                                   # Keeps the window open until we click exit
