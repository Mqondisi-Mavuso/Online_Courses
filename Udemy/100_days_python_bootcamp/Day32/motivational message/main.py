# sending email for motivation
import smtplib
import datetime as dt
from random import choice


# for retrieving the date and time
now = dt.datetime.now()                 # returns the class for current date and time
day_of_the_week = now.weekday()         # returns the day of the week starting from 0

# for retrieving the randon quote from the text file
with open("quotes.txt") as text_file:
    quotes = text_file.readlines()

# sending the email with the random quote
my_email = "mavusomqondisi@gmail.com"
password = "bgrrqsjcusdknsmb"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()                           # for encryption purposes
    connection.login(user=my_email, password=password)      # to logging my gmail account
    if day_of_the_week == 4:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nkhambulecelumusa3@gmail.com",
            msg=f"Subject:Morning Motivation from your lover\n\n{choice(quotes)}."
        )
