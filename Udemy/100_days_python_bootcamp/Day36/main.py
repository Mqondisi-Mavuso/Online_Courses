import requests
from newsapi import NewsApiClient
import itertools
import time

STOCK = "Amway"
COMPANY_NAME = "Amway"

api_key_alpha_vantage= "7Z4L3XBAPF5T4ABG"
api_key_news = "627e693128694d3c9c765bfd939c788d"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
    "interval": "60min",
    "apikey": api_key_alpha_vantage
}

news_parameters = {
    "q": "apple",
    "from": "2022-08-11",
    "to": "2022-08-12",
    "sortBy": "popularity",
    "apiKey": api_key_news
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
alpha_data = response.json()

print(alpha_data)
# first_two_days = dict(itertools.islice(alpha_data["Time Series FX (60min)"].items(),2))
yesterday_close_value = float(alpha_data["Time Series (Daily)"]["2022-08-12"]["4. close"])
previousday_close_value = float(alpha_data["Time Series (Daily)"]["2022-08-11"]["4. close"])

percentage_diff = round(((yesterday_close_value - previousday_close_value)/previousday_close_value) * 100, 1)

print(f"Yesterday's midday value market: {yesterday_close_value}")
print(f"Previous day mid\day market value: {previousday_close_value}")
#
# print(percentage_diff)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


if -2.0 > percentage_diff or percentage_diff > 2.0:
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()

    print(news_data)
else:
    pass

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
