# Automated email birthday wishes project
# day 32 of 100
from random import choice
import datetime as dt
import smtplib, os
import pandas as pd



# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
the_month = now.month
the_day = now.day

try:
    df = pd.read_csv("birthdays.csv")
except FileNotFoundError as error:
    print(f"{error}")
else:
    correct_month = df[df.month == the_month]
    correct_day = df[df.day == the_day]
    if correct_month is not None and correct_day is not None:
        recipient = correct_month.name
        my_email = "mavusomqondisi@gmail.com"
        password = "bgrrqsjcusdknsmb"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # for encryption purposes
            connection.login(user=my_email, password=password)  # to logging my gmail account
            try:
                dir = "D://Fortune/Education/Online_courses/Udemy/100_days_python_bootcamp/Day32/letter_templates"
                message = pd.read_csv(f"letter_templates/{choice(os.listdir(dir))}", index_col=False)
                message.drop(message.columns[len(message.columns) - 1], axis=1, inplace=True)      # remove last column
            except FileNotFoundError as error:
                print(f"{error}")
            else:
                # connection.sendmail(
                #     from_addr=my_email,
                #     to_addrs= correct_month.email,
                #     msg=f"Subject:Birthday Wishes\n\n{message}."
                # )
                print(message)



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




