import requests
from datetime import datetime
from time import sleep
from Message_Class import SendEmail

my_lat = 41.642566
my_lng = 42.981694


def tell_location():
    iss_now = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_now.raise_for_status()
    df = iss_now.json()
    longitude = float(df["iss_position"]["longitude"])
    latitude = float(df["iss_position"]["latitude"])
    if (latitude - 5 <= my_lat <= latitude + 5) and (longitude - 5 <= my_lng <= longitude + 5):
        return True


def tell_night():
    my_parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")
    sunset = data["results"]["sunset"].split("T")
    sunrise_hour = int(sunrise[1].split(":")[0])
    sunset_hour = int(sunset[1].split(":")[0])

    now = datetime.now()
    current_hour = now.hour

    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True


while True:
    sleep(60)
    if tell_location() and tell_night():
        msg_hand = SendEmail(subject="Warning", body="Go Outside, ISS is OverHead!")
        msg_hand.send_mail()
