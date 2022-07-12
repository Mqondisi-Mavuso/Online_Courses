# Password manager project
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]     # list comprehension
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers      # concatenate the lists
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)                                            # for copying the password onto the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():                                 # this is for saving the data into the text file
    website = web_entry.get()                     # This retrieves the data from the entries
    email = mail_entry.get()
    password_ = pass_entry.get()

    if len(website) == 0 or len(password_) == 0:
        messagebox.showerror(title="Incorrect Entry", message=f"You cannot leave any fields empty")

    else:
        # pop up message will show up for user to confirm whether it is correct or not
        correct_data = messagebox.askokcancel(title=website, message=f"Your details: \nEmail: {email}"
                                                                     f"\nPassword: {password_} \nIs it okay to save?")
        if correct_data:
            # exception handling 
            try:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password_}\n")
                    web_entry.delete(0, END)
                    pass_entry.delete(0, END)
            except FileNotFoundError:
                print("There was  an error")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")              # convert the normal image to PhotoImage
canvas.create_image(100, 100, image=logo_img)       # this expects a tuple
canvas.grid(column=1, row=0)                        # this is for placing the image/canvas


web_label = Label(text="Website:", font=("Times New Roman", 13))
web_label.grid(row=1, column=0)
web_entry = Entry(width=42)
web_entry.focus()               # this is to help focus the cursor when we run code
web_entry.grid(row=1, column=1, columnspan=2)
# print("This is the website entry: " %web_entry.get())

mail_label = Label(text="Email/Username:", font=("Times New Roman", 13))
mail_label.grid(row=2, column=0)
mail_entry = Entry(width=42)
mail_entry.insert(0, "fortunemavuso4@gmail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:", font=("Times New Roman", 13))
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=27)
pass_entry.grid(row=3, column=1)

gen_button = Button(text="Generate Password", highlightthickness=0, font=("Times New Roman", 8), command=generate)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
