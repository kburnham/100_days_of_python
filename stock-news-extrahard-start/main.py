import requests
import pandas as pd
import datetime as dt
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALERT_THRESHOLD = .05

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_endpoint = url = 'https://www.alphavantage.co/query'
#?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
stock_parameters = {"function": "TIME_SERIES_INTRADAY",
                    "symbol": STOCK,
                    "interval": "60min",
                    "apikey": "GZMQWG20Y3BPMUSV"}

r = requests.get(url, params=stock_parameters)
data = r.json()
df = pd.DataFrame(data['Time Series (60min)']).transpose()
df = df.set_index(pd.to_datetime(df.index))
df['datetime'] = df.index

df.columns = ['open', 'high', 'low', 'close', 'volume', 'datetime']
yesterday = dt.datetime.today() - dt.timedelta(days = 1)
two_days_ago = dt.datetime.today() - dt.timedelta(days = 2)

two_days_ago_open = float(df.loc[df['datetime'].dt.date == two_days_ago.date()]['open'][-1])
yesterday_close = float(df.loc[df['datetime'].dt.date == yesterday.date()]['close'][-1])

change = round((two_days_ago_open - yesterday_close) / two_days_ago_open, 2)

alert = True if abs(change) >= ALERT_THRESHOLD else False


if alert:


    ## STEP 2: Use https://newsapi.org
    yesterday_string = str(yesterday.date())
    news_api_key = 'b349d5c375034aad9a223eb51937091a'
    news_endpoint = 'https://newsapi.org/v2/everything'
    news_parameters = {"q": COMPANY_NAME,
                    "from": yesterday_string,
                    "apikey": news_api_key,
                    "pageSize": 3}

    news_response = requests.get(news_endpoint, params=news_parameters)

    len(news_response.json()['articles'])

    article = news_response.json()['articles'][1]
    articles = news_response.json()['articles']

    def summarize_articles(articles, change):
        indicator = "🔺" if change > 0 else "🔻"
        output = ""
        for article in articles:
            headline = article['title']
            summary = article['content'][:200]
            newline = '\n'
            article_summary = f'Headline: {headline}{os.linesep}\
                Brief: {summary}{os.linesep}'
            output += article_summary
        header = f'{STOCK}: {indicator}{round(change, 2)*100}%{os.linesep}'
        return(header + output)

    article_summary = summarize_articles(articles, change)

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    twilio_number = '+17752966524'
    twilio_account_sid = 'AC482479ab09970b55194dcae99d6a5d5b'
    twilio_auth_token = 'd336a743ad8740d54713550454e5ada1'
    twilio_recipient = '+15125966958'
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages \
                    .create(
                        body=article_summary,
                        from_=twilio_number,
                        to=twilio_recipient
                    )



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

