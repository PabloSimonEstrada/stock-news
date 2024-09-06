import requests
import datetime
import os
from datetime import timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_NEWS = "8c0de4132e5b40f09f35ec9f363114ce"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "symbol": STOCK_NAME,
    "apikey": "50YVY7KY4MTFFOOI",
    "function": "TIME_SERIES_DAILY"
}

today = datetime.date.today()
yesterday = today - timedelta(days=1)
before_yesterday = yesterday - timedelta(days=1)

parameters_news = {
    "q": "tesla",
    "from": yesterday,
    "apiKey": API_KEY_NEWS,
    "language": "en"
}

yesterday = str(yesterday)
before_yesterday = str(before_yesterday)
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()
yesterday_closing_price = data['Time Series (Daily)'][yesterday]["4. close"]

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_closing_price = data['Time Series (Daily)'][before_yesterday]["4. close"]
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
absolute_difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)

up_down = None
if absolute_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = abs(absolute_difference) / (float(before_yesterday_closing_price)) * 100
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_difference > 5:
    response_two = requests.get(NEWS_ENDPOINT, parameters_news)
    articles = response_two.json()["articles"]
    three_articles = articles[:3]

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    formated_articles = [f"{STOCK_NAME}: {up_down}{round(percentage_difference)}% \n Headline: {article['title']}. \nBrief: {article['description']} " for article in three_articles]
    print(formated_articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    account_sid = 'AC6a69c751c9c0d848a5dd79ff8e5f27ca'
    auth_token = '05651360fa07f6b65522a3f2915552c9'
    client = Client(account_sid, auth_token)
    for article in formated_articles:
        message = client.messages.create(
            body=article,
            from_='+14159416079',
            to='+353830718535')

    print(message.sid)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
