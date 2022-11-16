import requests
from SMS_Class import SendEmail
import os


my_key = os.environ.get("API_KEY")
my_lat = 40.839981
my_lon = 14.252540
my_parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": my_key
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=my_parameters)
response.raise_for_status()
data = response.json()["list"][0:12]

rain = False
for forcast in data:
    if forcast["weather"][0]["id"] < 700:
        rain = True
    else:
        rain = False

if rain:
    send_tool = SendEmail(subject="ForeCast", body="It is going to rain, Do not forget an Umbrella!")
    send_tool.send_mail()

