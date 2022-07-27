import requests
from datetime import datetime as dt

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
    if time_now >= lt_sunset and time_now < 24:
        return True
    elif time_now < lt_sunrise:
        return True
    else:
        return False


# ---------------------------------Getting local time and positioin ---------------------------
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

# --------------------------SEND E-MAIL------------------------------------------#
if iss_above() and is_night():
    pass

