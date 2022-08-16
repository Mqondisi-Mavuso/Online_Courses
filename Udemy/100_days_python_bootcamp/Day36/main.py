import requests
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

api_key_alpha_vantage = "7Z4L3XBAPF5T4ABG"
api_key_news = "627e693128694d3c9c765bfd939c788d"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": api_key_alpha_vantage
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": api_key_news
}

twilio_api_key = "SK8c0f01671c4b3b22c11f547a9f64cf85"
twilio_account_sid = "AC10b33f5534d919776cf0e16ed8bc81f9"
twilio_auth_token = "8bdfe9cd4bbc4e6cff88844570403b17"
twilio_number = "+18593282421"
twilio_recovery_code = "lTGyyU2nftGITYcFiSV9xFv8ESYV8-ClDGKhoIK_"

twilio_parameters = {
    "appid": twilio_api_key,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
alpha_data = response.json()["Time Series (Daily)"]

list_data = [value for (key, value) in alpha_data.items()]          # using list comprehension to convert dict to list
yesterday_dict = list_data[0]
yest_close_value = float(yesterday_dict["4. close"])
previous_day_dict = list_data[1]
previousday_close_value = float(previous_day_dict["4. close"])

percentage_diff = round(((yest_close_value - previousday_close_value)/previousday_close_value) * 100, 1)
#
print(f"Yesterday's midday value market: {yest_close_value}")
print(f"Previous day mid\day market value: {previousday_close_value}")
print(percentage_diff)

# ## STEP 2: Use https://newsapi.org
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#
#
if 0 > percentage_diff or percentage_diff > 0:
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()["articles"][:3]

    if percentage_diff < 0:
        final_articles = [
            f"AAPL 🔻{percentage_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
            for article in news_data]
    else:
        final_articles = [
            f"AAPL 🔺{percentage_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
            article in news_data]

    client = Client(twilio_account_sid, twilio_auth_token)
    for message_body in final_articles:
        print(message_body)
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to='+8860988030913'
        )

        # print(message.error_message)
else:
    pass

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this:

