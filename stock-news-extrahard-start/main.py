import os
import requests
import html
from twilio.rest import Client, TwilioHttpClient
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# # Environment variable setup: type "export API_KEY_STOCK=(key goes here)" on pythonanywhere console
# API_KEY_STOCK = os.environ.get("API_KEY_STOCK")
API_KEY_STOCK = "G2O4P39TL3CX7DRQ"
stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'

# # Environment variable setup: type "export API_KEY_NEWS=(key goes here)" on pythonanywhere console
# API_KEY_NEWS = os.environ.get("API_KEY_NEWS")
API_KEY_NEWS = "f4a2b81e7b214655b97316179c839542"
news_url = 'https://newsapi.org/v2/everything'

ACCOUNT_SID = 'AC839f4511b553ec694045277b99a12e8a'
# # Environment variable setup: type "export AUTH_TOKEN=(key goes here)" on pythonanywhere console
# AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
AUTH_TOKEN = '9c6592f9d842ac1c928e243a60163ac1'
TWILIO_NUM = '+18597805147'


def stock():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": API_KEY_STOCK
    }
    stock_api = requests.get(url=stock_url, params=stock_params)
    stock_api.raise_for_status()
    stock_data = stock_api.json()["Time Series (Daily)"]

    today = datetime.now().date() - timedelta(1)
    yesterday = today - timedelta(2)
    today = today.strftime("%Y-%m-%d")
    yesterday = yesterday.strftime("%Y-%m-%d")

    today_stock = float(stock_data[today]["4. close"])
    yesterday_stock = float(stock_data[yesterday]["4. close"])
    diff = round((today_stock - yesterday_stock) / today_stock * 100, 2)
    if diff > 0:
        symbol = "🔺"
    else:
        symbol = "🔻"
    return f"{COMPANY_NAME}: {symbol}{diff}%\n"


def news():
    news_params = {
        "apiKey": API_KEY_NEWS,
        "q": COMPANY_NAME,
        "pageSize": 1
    }

    news_api = requests.get(url=news_url, params=news_params)
    news_api.raise_for_status()
    news_data = news_api.json()["articles"][0]
    title = news_data["title"]
    body = news_data["url"]
    return html.unescape(f"Headline: {title}\nCheck on site: {body}\n")


def text():
    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)

    client.messages.create(
        to='17149049006',
        from_=TWILIO_NUM,
        body=stock() + news(),
    )


text()
# print(news())


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

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