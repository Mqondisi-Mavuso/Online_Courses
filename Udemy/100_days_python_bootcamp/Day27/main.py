from tkinter import *

window = Tk()
window.title("Mile to Km Converter")          # For changing the title of the window
window.minsize(width=500, height=300)

# label
click_variable = ""
answer = Label(text="", font=("Arial", 24, "bold"))
answer.grid(column=1, row=1)                # This allows the label to be shown on the screen

miles = Label(text="Miles", font=("Arial", 24, "bold"))
miles.grid(column=2, row=0)                # This allows the label to be shown on the screen

kilometers = Label(text="Km", font=("Arial", 24, "bold"))
kilometers.grid(column=2, row=1)                # This allows the label to be shown on the screen

equals = Label(text="is equal to", font=("Arial", 24, "bold"))
equals.grid(column=0, row=1)                # This allows the label to be shown on the screen

def click():
    outcome = round(float(entry.get())*1.60934, 2)      # gets the string from the entry box and calculate the Km
    answer.config(text =str(outcome))                   # change the answer label text to the answer

my_button = Button(text="Calculate", command=click)     # command listens to the mouse click from use and call click()
my_button.grid(column=1, row=2)

entry = Entry()
entry.grid(column=1, row=0)

window.mainloop()