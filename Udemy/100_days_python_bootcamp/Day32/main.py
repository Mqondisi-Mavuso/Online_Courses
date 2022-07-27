# day 33
# API endpoints, ISS above notifier 

import requests
from datetime import datetime as dt
import smtplib
import time

LATITUDE = 23.901471
LONGITUDE = 121.546151
LOCAL_UTC_OFFSET = 8


def utc_to_local(utc_hour):
    # this is for converting from UCT to my local timezone
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def iss_above():
    if LATITUDE - 5 <= iss_latitude <= LATITUDE + 5:
        if LONGITUDE - 5 <= iss_longitude <= LONGITUDE + 5:
            return True
    else:
        return False


def is_night():
    if time_now >= lt_sunset or time_now < lt_sunrise:
        return True
    else:
        return False


# ---------------------------------Getting local time and position ---------------------------
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}

response = requests.get(url="http://api.sunrise-sunset.org/json?", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

lt_sunrise = utc_to_local(sunrise)
lt_sunset = utc_to_local(sunset)
time_now = dt.now().time().hour

# -------------------------------------------------Getting ISS location --------------------
iss_data = requests.get(url="http://api.open-notify.org/iss-now.json").json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

# --------------------------SEND E-MAIL----------------------------------------------------#
# this while loop allows the code to run forever in the background every 60 seconds
while True:
    time.sleep(60)
    if iss_above() and is_night():
        my_email = "mavusomqondisi@gmail.com"
        password = "bgrrqsjcusdknsmb"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # for encryption purposes
            connection.login(user=my_email, password=password)  # to logging my gmail account
            connection.sendmail(
                from_addr=my_email,
                to_addrs="fortunemavuso4@gmail.com",
                msg=f"Subject:International Space Station (ISS) \n\n Look up the ISS is currently above you!."
            )
