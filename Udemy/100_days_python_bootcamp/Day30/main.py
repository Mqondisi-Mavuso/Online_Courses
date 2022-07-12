# day 29  and 30 of 100
# Password manager project
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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

    # json file, this will be used to store the data in json format
    new_data = {
        website: {
            "email": email,
            "password": password_
        }
    }

    if len(website) == 0 or len(password_) == 0:
        messagebox.showerror(title="Incorrect Entry", message=f"You cannot leave any fields empty")

    else:
        # pop up message will show up for user to confirm whether it is correct or not
        correct_data = messagebox.askokcancel(title=website, message=f"Your details: \nEmail: {email}"
                                                                     f"\nPassword: {password_} \nIs it okay to save?")
        if correct_data:
            # exception handling to avoid programme crush
            try:
                with open("data.json", "r") as data_file:
                    # this is for reading from the file
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            # this will be triggered if everything passes on the try statement
            else:
                # for updating the old data with new data
                data.update(new_data)

                # for saving the new data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            # this will run every time
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #


def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # this is for reading from the file
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title=f"{website}", message=f"File is not found")

    # this will execute if the try block passes
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"email: {email} \npassword: {password}")
        else:
            messagebox.showinfo(title=f"{website}", message=f"Data not found in file")
    finally:
        web_entry.delete(0, END)
        pass_entry.delete(0, END)
        pyperclip.copy(data[website]["password"])  # for copying the password onto the clipboard


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

search_button = Button(text="Search", highlightthickness=0,
                       font=("Times New Roman", 8), command=find_password, width=14)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", highlightthickness=0, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
