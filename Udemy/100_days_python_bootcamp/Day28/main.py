from tkinter import *
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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", font=("Times New Roman", 24, "bold"))
timer.config(bg=YELLOW)
timer.config(fg=GREEN)
timer.grid(row=0, column=1)                # This allows the label to be shown on the screen

check_box = Label(text="✔", font=("Times New Roman", 24, "bold"))
check_box.config(bg=YELLOW)
check_box.config(fg=GREEN)
check_box.grid(row=3, column=1)                # This allows the label to be shown on the screen

def click():
    outcome = round(float(entry.get())*1.60934, 2)      # gets the string from the entry box and calculate the Km
    answer.config(text =str(outcome))                   # change the answer label text to the answer

start_button = Button(text="Start", command=click, highlightthickness=0)     # command listens to the mouse click from use and call click()
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=click, highlightthickness=0)     # command listens to the mouse click from use and call click()
reset_button.grid(row=2, column=2)



window.mainloop()
