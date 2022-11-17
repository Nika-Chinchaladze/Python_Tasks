import requests
from datetime import datetime
from html import unescape
import os
from Notification_Class import SendEmail

current = datetime.now()
yesterday = f"{current.year}-{current.month}-{current.day-1}"
previous_yesterday = f"{current.year}-{current.month}-{current.day-2}"

# =============================== STOCK DATA THROUGH DAYS =============================== #
my_url_stock = "https://www.alphavantage.co/query"
my_api_stock = os.environ.get("STOCK_API")
my_function = "TIME_SERIES_DAILY_ADJUSTED"
my_symbol = "TSLA"
my_parameters = {
    "function": my_function,
    "symbol": my_symbol,
    "apikey": my_api_stock
}
response_stock = requests.get(url=my_url_stock, params=my_parameters)
response_stock.raise_for_status()
data = response_stock.json()["Time Series (Daily)"]
day_before_one = float(data[yesterday]["4. close"])
day_before_two = float(data[previous_yesterday]["4. close"])

# calculation part:
difference = abs(day_before_one - day_before_two)
percent = round((difference / day_before_one) * 100, 2)
answer = ""
if day_before_one > day_before_two:
    answer = f"🔺 prices have increased by {round(percent)}%"
else:
    answer = f"🔻 prices have decreased by {round(percent)}%"


# =============================== NEWS THROUGH DAYS : SEND NOTIFICATION ============================ #
if percent >= 3:
    my_url_news = "https://newsapi.org/v2/everything"
    my_company = "Tesla Inc"
    my_date = yesterday
    my_sort = "popularity"
    my_api_news = os.environ.get("NEWS_API")
    my_parameters = {
        "q": my_company,
        "from": my_date,
        "sortBy": my_sort,
        "apiKey": my_api_news
    }
    response_news = requests.get(url=my_url_news, params=my_parameters)
    response_news.raise_for_status()
    data = response_news.json()["articles"][0]
    # message part:
    title = data["title"]
    news = unescape(data["description"])

    message_body = f"{answer} \nTitle: {title} \nNews: \n{news}"

    send_tool = SendEmail(subject="Info", body=message_body)
    send_tool.send_mail()
    print("message sent")
else:
    print("mission completed")
