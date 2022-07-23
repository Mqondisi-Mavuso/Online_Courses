# Automated email birthday wishes project
# day 32 of 100
import random
import datetime as dt
import smtplib
import pandas as pd

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)                  # making a date tuple

try:
    data = pd.read_csv("birthdays.csv")
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
except FileNotFoundError as error:
    print(f"{error}")
else:
    if today_tuple in birthdays_dict:                   # checks if today's date matches anyone's birthday
        recipient = birthdays_dict[today_tuple]       # stores the record of the person with the date we're looking for
        print(recipient)
        file_dir = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        try:
            with open(file_dir) as letter_file:
                message = letter_file.read()
                message = message.replace("[NAME]", recipient["name"])
        except FileNotFoundError as the_error:
            print(the_error)
        else:
            my_email = "mavusomqondisi@gmail.com"
            password = "bgrrqsjcusdknsmb"

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()                                                   # for encryption purposes
                connection.login(user=my_email, password=password)                      # to logging my gmail account
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=recipient["email"],
                    msg=f"Subject:Birthday Wishes\n\n{message}."
                )
